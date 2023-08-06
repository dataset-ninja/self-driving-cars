# # https://www.kaggle.com/datasets/kumaresanmanickavelu/lyft-udacity-challenge?datasetId=27201&sortBy=voteCount

import glob
import os

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from supervisely.io.fs import get_file_name, get_file_name_with_ext


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    pass

    dataset_path = "APP_DATA/archive"
    batch_size = 30
    images_folder_name = "CameraRGB"
    masks_folder_name = "CameraSeg"

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        mask_name = get_file_name_with_ext(image_path)
        mask_path = os.path.join(masks_path, mask_name)
        ann_np = sly.imaging.image.read(mask_path)[:, :, 0]
        unique_idx = np.unique(ann_np)

        for i in unique_idx:
            obj_mask = ann_np == i
            ret, curr_mask = connectedComponents(obj_mask.astype("uint8"), connectivity=8)
            for j in range(1, ret):
                obj_mask = curr_mask == j
                curr_bitmap = sly.Bitmap(obj_mask)
                if curr_bitmap.area > 50:
                    curr_obj_class = idx_to_obj_class[i]
                    curr_label = sly.Label(curr_bitmap, curr_obj_class)
                    labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class_sky = sly.ObjClass("sky", sly.Bitmap)
    obj_class_pole = sly.ObjClass("pole", sly.Bitmap)
    obj_class_building = sly.ObjClass("building", sly.Bitmap)
    obj_class_road = sly.ObjClass("road", sly.Bitmap)
    obj_class_tree = sly.ObjClass("tree", sly.Bitmap)
    obj_class_sidewalk = sly.ObjClass("sidewalk", sly.Bitmap)
    obj_class_road_markings = sly.ObjClass("road markings", sly.Bitmap)
    obj_class_car = sly.ObjClass("car", sly.Bitmap)
    obj_class_fence = sly.ObjClass("fence", sly.Bitmap)
    obj_class_pedestrian = sly.ObjClass("pedestrian", sly.Bitmap)
    obj_class_street = sly.ObjClass("street infrastructure ", sly.Bitmap)
    obj_class_wall = sly.ObjClass("wall", sly.Bitmap)
    obj_class_traffic = sly.ObjClass("traffic", sly.Bitmap)

    idx_to_obj_class = {
        0: obj_class_sky,
        1: obj_class_building,
        2: obj_class_fence,
        3: obj_class_street,
        4: obj_class_pedestrian,
        5: obj_class_pole,
        6: obj_class_road_markings,
        7: obj_class_road,
        8: obj_class_sidewalk,
        9: obj_class_tree,
        10: obj_class_car,
        11: obj_class_wall,
        12: obj_class_traffic,
    }

    obj_class_collection = sly.ObjClassCollection(
        [
            obj_class_sky,
            obj_class_pole,
            obj_class_building,
            obj_class_road,
            obj_class_tree,
            obj_class_sidewalk,
            obj_class_road_markings,
            obj_class_car,
            obj_class_fence,
            obj_class_pedestrian,
            obj_class_street,
            obj_class_wall,
            obj_class_traffic,
        ]
    )

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(project.id, meta.to_json())

    datasets_pathes = glob.glob(dataset_path + "/*/*")
    ds_names = []

    dataset = api.dataset.create(project.id, "ds", change_name_if_conflict=True)
    progress = sly.Progress("Create dataset ds", 5000)

    for curr_ds_path in datasets_pathes:
        ds_name = get_file_name(curr_ds_path)
        if (
            ds_name not in ds_names
        ):  # same data calls dataa and dataA, project contain 5 datasets(1000 img each), not 10...
            ds_names.append(ds_name)

            images_path = os.path.join(curr_ds_path, images_folder_name)
            masks_path = os.path.join(curr_ds_path, masks_folder_name)
            images_names = os.listdir(images_path)

            for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                images_pathes_batch = [
                    os.path.join(images_path, image_path) for image_path in img_names_batch
                ]

                anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]

                img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                api.annotation.upload_anns(img_ids, anns_batch)

                progress.iters_done_report(len(img_names_batch))

    return project
