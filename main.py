import math
import re

import cv2
import gradio as gr
import matplotlib
import matplotlib.pyplot as plt
import mediapipe as mp
import nltk
import numpy as np
import pandas as pd
import pytesseract
import seaborn as sns
import timm
import torch
import whisper
from deepface import DeepFace
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from PIL import Image, ImageDraw
from pytesseract import Output
from pyzbar.pyzbar import decode
from scipy.stats import pearsonr
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from textblob import TextBlob
from textblob_nl import PatternAnalyzer, PatternTagger
from torchvision import transforms
from ultralytics import YOLO

matplotlib.use("TkAgg")  # Alternative: "Agg" for headless mode

