# Generated by Django 4.2.1 on 2023-05-26 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            ALTER TABLE core_profile AUTO_INCREMENT = 1;
            INSERT INTO core_profile (email, isHidden) VALUES ('1@email.com', false);
            INSERT INTO core_profile (email, isHidden) VALUES ('2@email.com', false);
            INSERT INTO core_profile (email, isHidden) VALUES ('3@email.com', false);
            INSERT INTO core_profile (email, isHidden) VALUES ('4@email.com', false);
            INSERT INTO core_profile (email, isHidden) VALUES ('5@email.com', false);
            INSERT INTO core_profile (email, isHidden) VALUES ('6@email.com', false);
            INSERT INTO core_profile (email, isHidden) VALUES ('7@email.com', false);
            INSERT INTO core_profile (email, isHidden) VALUES ('8@email.com', false);
            INSERT INTO core_profile (email, isHidden) VALUES ('dblivechecker@email.com', false);

        """, """
            DELETE FROM core_profile;
        """)
    ]