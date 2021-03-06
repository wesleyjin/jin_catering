# Generated by Django 2.1.5 on 2019-02-24 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=18)),
                ('address', models.CharField(blank=True, max_length=60)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('notes', models.TextField(blank=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredient_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=100)),
                ('ingredient_type', models.CharField(max_length=30)),
                ('in_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=30)),
                ('item_type', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=38)),
                ('size', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=30)),
                ('items', models.ManyToManyField(to='order_management.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('deliver_date', models.DateField()),
                ('total_sales', models.DecimalField(decimal_places=2, max_digits=38)),
                ('is_delivery', models.BooleanField(blank=True, null=True)),
                ('paid', models.BooleanField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order_management.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=38)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order_management.Item')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order_management.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('packaging_id', models.AutoField(primary_key=True, serialize=False)),
                ('packaging_type', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=10)),
                ('in_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('recipe_name', models.CharField(max_length=30)),
                ('portions', models.IntegerField()),
                ('time_to_cook', models.DurationField(blank=True, null=True)),
                ('directions', models.TextField(blank=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('ingredients', models.ManyToManyField(to='order_management.Ingredient')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order_management.Item')),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='packaging',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order_management.Packaging'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='order_management.OrderItem', to='order_management.Item'),
        ),
    ]
