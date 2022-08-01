# Generated by Django 4.0.4 on 2022-05-31 04:07

from django.db import migrations, models
import village.validators


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attacktechnique',
            name='attack_range',
            field=models.CharField(max_length=5, validators=[village.validators.attack_technique_attack_range_validator]),
        ),
        migrations.AlterField(
            model_name='chunin',
            name='chunin_exam_grade',
            field=models.IntegerField(validators=[village.validators.exam_grade_validator]),
        ),
        migrations.AlterField(
            model_name='curativetechnique',
            name='curing_speed',
            field=models.CharField(max_length=5, validators=[village.validators.curative_technique_curing_speed_range_validator]),
        ),
        migrations.AlterField(
            model_name='jounin',
            name='jounin_exam_grade',
            field=models.IntegerField(validators=[village.validators.exam_grade_validator]),
        ),
        migrations.AlterField(
            model_name='mission',
            name='churikens_amount',
            field=models.IntegerField(validators=[village.validators.amount_validator]),
        ),
        migrations.AlterField(
            model_name='mission',
            name='explosive_seals_amount',
            field=models.IntegerField(validators=[village.validators.amount_validator]),
        ),
        migrations.AlterField(
            model_name='mission',
            name='kunais_amount',
            field=models.IntegerField(validators=[village.validators.amount_validator]),
        ),
        migrations.AlterField(
            model_name='mission',
            name='rank_m',
            field=models.CharField(max_length=1, validators=[village.validators.rank_validator]),
        ),
        migrations.AlterField(
            model_name='mission',
            name='reward_yens',
            field=models.IntegerField(validators=[village.validators.yen_validator]),
        ),
        migrations.AlterField(
            model_name='ninja',
            name='max_chakra_amount',
            field=models.IntegerField(validators=[village.validators.ninja_chakra_validator]),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=1, validators=[village.validators.person_gender_validator]),
        ),
        migrations.AlterField(
            model_name='technique',
            name='chakra_amount',
            field=models.IntegerField(validators=[village.validators.technique_chakra_validator]),
        ),
        migrations.AlterField(
            model_name='technique',
            name='element',
            field=models.CharField(max_length=20, validators=[village.validators.technique_element_validator]),
        ),
    ]
