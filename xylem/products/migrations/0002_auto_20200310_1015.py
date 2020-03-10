# Generated by Django 2.2.10 on 2020-03-10 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='category/thumbnail'),
        ),
        migrations.AddField(
            model_name='product',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.PositiveIntegerField(default=5, verbose_name='Stock Keeping Unit'),
        ),
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='category/None/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.Category')),
            ],
        ),
    ]
