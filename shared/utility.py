from django.core.exceptions import ValidationError
import re

LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('zh', 'Chinese'),
    ('es', 'Spanish'),
    ('hi', 'Hindi'),
    ('ar', 'Arabic'),
    ('bn', 'Bengali'),
    ('pt', 'Portuguese'),
    ('ru', 'Russian'),
    ('ja', 'Japanese'),
    ('de', 'German'),
    ('ko', 'Korean'),
    ('fr', 'French'),
    ('tr', 'Turkish'),
    ('it', 'Italian'),
    ('vi', 'Vietnamese'),
    ('th', 'Thai'),
    ('pl', 'Polish'),
    ('uk', 'Ukrainian'),
    ('nl', 'Dutch'),
    ('fa', 'Persian'),
    ('sv', 'Swedish'),
    ('fi', 'Finnish'),
    ('ro', 'Romanian'),
    ('he', 'Hebrew'),
    ('id', 'Indonesian'),
    ('cs', 'Czech'),
    ('hu', 'Hungarian'),
    ('el', 'Greek'),
    ('da', 'Danish'),
    ('no', 'Norwegian'),
    ('sr', 'Serbian'),
    ('sk', 'Slovak'),
    ('bg', 'Bulgarian'),
    ('hr', 'Croatian'),
    ('ms', 'Malay'),
    ('lt', 'Lithuanian'),
    ('lv', 'Latvian'),
    ('sl', 'Slovenian'),
    ('et', 'Estonian'),
    ('is', 'Icelandic'),
    ('tl', 'Tagalog'),
    ('ur', 'Urdu'),
    ('ta', 'Tamil'),
    ('te', 'Telugu'),
    ('kn', 'Kannada'),
    ('ml', 'Malayalam'),
    ('mr', 'Marathi'),
    ('gu', 'Gujarati'),
    ('pa', 'Punjabi'),
    ('sw', 'Swahili'),
    ('yo', 'Yoruba'),
    ('ha', 'Hausa'),
    ('ig', 'Igbo'),
    ('am', 'Amharic'),
    ('ne', 'Nepali'),
    ('si', 'Sinhala'),
    ('km', 'Khmer'),
    ('my', 'Burmese'),
    ('lo', 'Lao'),
    ('mn', 'Mongolian'),
    ('ka', 'Georgian'),
    ('hy', 'Armenian'),
    ('az', 'Azerbaijani'),
    ('kk', 'Kazakh'),
    ('uz', 'Uzbek'),
    ('tg', 'Tajik'),
    ('tk', 'Turkmen'),
    ('ky', 'Kyrgyz'),
    ('ps', 'Pashto'),
    ('dv', 'Dhivehi'),
    ('bo', 'Tibetan'),
    ('ku', 'Kurdish'),
    ('eu', 'Basque'),
    ('gl', 'Galician'),
    ('cy', 'Welsh'),
    ('gd', 'Scottish Gaelic'),
    ('ga', 'Irish'),
    ('mt', 'Maltese'),
    ('sq', 'Albanian'),
    ('bs', 'Bosnian'),
    ('mk', 'Macedonian'),
    ('xh', 'Xhosa'),
    ('zu', 'Zulu'),
    ('af', 'Afrikaans'),
    ('st', 'Sesotho'),
    ('tn', 'Tswana'),
    ('ts', 'Tsonga'),
    ('ve', 'Venda'),
    ('sn', 'Shona'),
    ('ny', 'Chichewa'),
    ('rw', 'Kinyarwanda'),
    ('ln', 'Lingala'),
    ('kg', 'Kongo'),
    ('fj', 'Fijian'),
    ('sm', 'Samoan'),
    ('to', 'Tongan'),
    ('mi', 'Māori'),
    ('haw', 'Hawaiian'),
    ('chr', 'Cherokee'),
    ('nv', 'Navajo'),
    ('oj', 'Ojibwe'),
]


def validate_username(value):
    # 1. Username uzunligi 128 belgidan oshmasligi kerak
    if len(value) > 128:
        raise ValidationError("Username uzunligi 128 belgidan oshmasligi kerak.")

    # 2. Username faqat kichik harflar, raqamlar, va maxsus belgilar (-, _) bo'lishi kerak
    if not re.match(r'^[a-z0-9_-]+$', value):
        raise ValidationError(
            "Username faqat kichik harflar, raqamlar, '_' va '-' belgilarini o'z ichiga olishi mumkin.")

    # 3. Username birinchi belgisi raqam bo'lmasligi kerak
    if value[0].isdigit():
        raise ValidationError("Username birinchi belgisi raqam bo'lmasligi kerak.")

    # 4. Username faqat alifbo va raqamlardan iborat bo'lishi kerak
    if not value.isalnum() and not any(c in value for c in "-_"):
        raise ValidationError(
            "Username faqat alifbo, raqamlar va '-' yoki '_' maxsus belgilarini o'z ichiga olishi mumkin.")



valid_image_types = ["jpg", "jpeg", "png", "webp", "heic", "heif"]