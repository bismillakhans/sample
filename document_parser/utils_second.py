import re

import cv2
import numpy as np
from django.conf import settings
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from nltk.corpus import stopwords
import tensorflow as tf
import pytesseract
import textacy

from document_parser.utils import label_map_util
from document_parser.utils import visualization_utils as vis_util

stop_words = set(stopwords.words('english'))


df = pd.read_csv(settings.TRAIN_URL, encoding = "ISO-8859-1")
df_data=df.content
df=df.drop(['content'],axis=1)


def final_result(res):
    SVC_pipe = {}
    for i, ivl in enumerate(df):
        # print(i,iv)
        SVC_pipe[ivl] = SVC_pipeline()
        SVC_pipe[ivl].fit(df_data, df[ivl])
    result = {}
    # res = [
        # "bismillakhans@gmail.com Roshna Manzil Chemmanoorkonam Vembayam P. O.695615 22 years old 0808 980 4597 Indian",
        # 'P ROJECTS U NDERTAKEN Heart disease prediction using SVM, Python 3.6 Microfinance Management System (B. Sc. Main Project) using Java Utility Management System (BSc. Mini Project) using PHP and My SQL']
    for x in res:
        for i, iv in enumerate(SVC_pipe):
            if SVC_pipe[iv].predict([x]):
                result[iv] = x

    return result


def SVC_pipeline():
    SVC_pipeline = Pipeline([
                    ('tfidf', TfidfVectorizer(stop_words=stop_words)),
                    ('clf', OneVsRestClassifier(LinearSVC(), n_jobs=1)),
                ])
    return SVC_pipeline
#
#
# def funcc():
#     SVC_pipeline_name = SVC_pipeline()
#     SVC_pipeline_name.fit(df_value, df['name'])
#
#     SVC_pipeline_achievements = SVC_pipeline()
#     SVC_pipeline_achievements.fit(df_value, df['achievements'])
#
#     SVC_pipeline_declaration = SVC_pipeline()
#     SVC_pipeline_declaration.fit(df_value, df['declaration'])
#
#     SVC_pipeline_education = SVC_pipeline()
#     SVC_pipeline_education.fit(df_value, df['education'])
#
#     SVC_pipeline_experience = SVC_pipeline()
#     SVC_pipeline_experience.fit(df_value, df['experience'])
#
#     SVC_pipeline_hobbies = SVC_pipeline()
#     SVC_pipeline_hobbies.fit(df_value, df['hobbies'])
#
#     SVC_pipeline_interest = SVC_pipeline()
#     SVC_pipeline_interest.fit(df_value, df['interest'])
#
#     SVC_pipeline_language = SVC_pipeline()
#     SVC_pipeline_language.fit(df_value, df['language'])
#
#     SVC_pipeline_objective = SVC_pipeline()
#     SVC_pipeline_objective.fit(df_value, df['objective'])
#
#     SVC_pipeline_personal_detail = SVC_pipeline()
#     SVC_pipeline_personal_detail.fit(df_value, df['personal detail'])
#
#     SVC_pipeline_project = SVC_pipeline()
#     SVC_pipeline_project.fit(df_value, df['project'])
#
#     SVC_pipeline_reference = SVC_pipeline()
#     SVC_pipeline_reference.fit(df_value, df['reference'])
#
#     SVC_pipeline_seminar = SVC_pipeline()
#     SVC_pipeline_seminar.fit(df_value, df['seminar'])
#
#     SVC_pipeline_soft_skill = SVC_pipeline()
#     SVC_pipeline_soft_skill.fit(df_value, df['soft skill'])
#
#     SVC_pipeline_technical_skill = SVC_pipeline()
#     SVC_pipeline_technical_skill.fit(df_value, df['technical skill'])
#
#     SVC_pipeline_training = SVC_pipeline()
#     SVC_pipeline_training.fit(df_value, df['training'])
#
#     SVC_pipeline_iv = SVC_pipeline()
#     SVC_pipeline_iv.fit(df_value, df['iv'])
#


def label_model():

    label_map = label_map_util.load_labelmap(settings.LABEL_URL)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=1, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
    return category_index


# def function2(PATH_TO_IMAGE):
#     label_map = label_map_util.load_labelmap(settings.LABEL_URL)
#     categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=1,
#                                                                 use_display_name=True)
#     category_index = label_map_util.create_category_index(categories)
#
#     detection_graph = tf.Graph()
#     with detection_graph.as_default():
#         od_graph_def = tf.GraphDef()
#         with tf.gfile.GFile(settings.LABEL_URL, 'rb') as fid:
#             serialized_graph = fid.read()
#             od_graph_def.ParseFromString(serialized_graph)
#             tf.import_graph_def(od_graph_def, name='')
#
#         sess = tf.Session(graph=detection_graph)
#
#     image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
#     detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
#     detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
#     detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
#     num_detections = detection_graph.get_tensor_by_name('num_detections:0')
#
#     # listing = os.listdir(PATH_TO_IMAGE)
#     result = []
#     # for image_list in listing:
#
#         # print(f"\n----------THE IMAGE IS {image_list}-------------\n")
#
#         # image = cv2.imread(os.path.join(PATH_TO_IMAGE, image_list))
#     image = cv2.imread(PATH_TO_IMAGE)
#     # im_height = image.shape[0]
#     # im_width = image.shape[1]
#     image_expanded = np.expand_dims(image, axis=0)
#     # print("Processing...")
#     (boxes, scores, classes, num) = sess.run(
#         [detection_boxes, detection_scores, detection_classes, num_detections],
#         feed_dict={image_tensor: image_expanded})
#
#     coordinates = vis_util.return_coordinates(
#         image,
#         np.squeeze(boxes),
#         np.squeeze(classes).astype(np.int32),
#         np.squeeze(scores),
#         category_index,
#         use_normalized_coordinates=True,
#         line_thickness=8,
#         min_score_thresh=0.80)
#     for x in coordinates:
#         ymin = x[0]
#         ymax = x[1]
#         xmin = x[2]
#         xmax = x[3]
#         new_image = image[ymin:ymax, xmin:xmax]
#         section = pytesseract.image_to_string(new_image)
#         result.append(
#             textacy.preprocess.remove_punct(section, marks=' \n  ___ ~ < ! # $ % ^ & * \( \) \{ \} \[ \] '))
#     return result





def function1(path):
    print(path)
    label_map = label_map_util.load_labelmap(settings.LABEL_URL)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=1,
                                                                use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(settings.TENSOR_URL, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)

    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    #     listing = os.listdir(PATH_TO_IMAGE)
    result = []
    image = cv2.imread(path)
    #     im_height = image.shape[0]
    #     im_width = image.shape[1]
    image_expanded = np.expand_dims(image, axis=0)
    #     print("Processing...")
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded})

    coordinates = vis_util.return_coordinates(
        image,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.80)
    for x in coordinates:
        ymin = x[0]
        ymax = x[1]
        xmin = x[2]
        xmax = x[3]
        new_image = image[ymin:ymax, xmin:xmax]
        section = pytesseract.image_to_string(new_image)
        result.append(textacy.preprocess.remove_punct(section, marks=' \n  ___ ~ < ! # $ % ^ & * \( \) \{ \} \[ \] '))
    return result


def extract_name(nlp_text):
    '''
    Helper function to extract name from spacy nlp text

    :param nlp_text: object of `spacy.tokens.doc.Doc`
    :param matcher: object of `spacy.matcher.Matcher`
    :return: string of full name
    '''
    dd={}
    for ent in nlp_text.ents:
        dd[ent.label_]=ent.text
    return dd



def extract_email(text):
    '''
    Helper function to extract email id from text

    :param text: plain text extracted from resume file
    '''
    #email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", text)
    email = re.findall("[\w\.-]+@[\w\.-]+", text)

    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None

# def extract_name(nlp_text):
#     '''
#     Helper function to extract name from spacy nlp text
#
#     :param nlp_text: object of `spacy.tokens.doc.Doc`
#     :param matcher: object of `spacy.matcher.Matcher`
#     :return: string of full name
#     '''
#
#     for ent in nlp_text.ents:
#         return ent.text

def extract_mobile_number(text):
    '''
    Helper function to extract mobile number from text

    :param text: plain text extracted from resume file
    :return: string of extracted mobile numbers
    '''
    # Found this complicated regex on : https://zapier.com/blog/extract-links-email-phone-regex/
    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), text)
    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return '+' + number
        else:
            return number




