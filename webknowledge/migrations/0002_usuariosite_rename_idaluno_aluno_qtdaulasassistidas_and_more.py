# Generated by Django 5.0.9 on 2024-11-08 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webknowledge", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Usuariosite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("idusuario", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("cpf", models.IntegerField(max_length=11)),
                ("datadenascimento", models.DateField()),
                ("nota", models.FloatField(max_length=3)),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name="aluno",
            old_name="idaluno",
            new_name="qtdaulasassistidas",
        ),
        migrations.RenameField(
            model_name="professor",
            old_name="idProfessor",
            new_name="qtdaulasfeitas",
        ),
        migrations.RemoveField(
            model_name="aluno",
            name="id",
        ),
        migrations.RemoveField(
            model_name="aluno",
            name="nome",
        ),
        migrations.RemoveField(
            model_name="avaliacao",
            name="idAvaliacao",
        ),
        migrations.AddField(
            model_name="avaliacao",
            name="comentario",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="professor",
            name="disciplina",
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="aluno",
            name="usuariosite_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="webknowledge.usuariosite",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="avaliacao",
            name="avaliada",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="webknowledge.usuariosite",
            ),
            preserve_default=False,
        ),
    ]