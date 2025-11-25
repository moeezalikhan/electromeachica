from django.db import migrations

def add_product_categories(apps, schema_editor):
    Categories = apps.get_model('products', 'Categories')
    data = [
        "Programable Logic Controller (PLC)",
        "Variable Frequency Drive (VFD)",
        "Hydraulic Valves",
        "Pneumatic Valves",
        "Sensors",
        "Actuators",
        "I/P Positioners",
        "Angle Transducer",
        "Human Machine Interface (HMI)",
        "Encoders",
        "Resolvers",
        "Embedded System",
    ]
    for item in data:
        Categories.objects.create(name=item)

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),  # initial migration that created models
    ]

    operations = [
        migrations.RunPython(add_product_categories),
    ]
