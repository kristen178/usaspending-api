# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-20 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_activities', '0015_financial_activities_oc'),
    ]

    update_object_class_sql = '''
        update financial_accounts_by_program_activity_object_class fa1
        set object_class_id = (
            select oc.id
            from financial_accounts_by_program_activity_object_class fa2
            join ref_object_class_code roc
            on fa2.object_class_old = roc.object_class
            join object_class oc
            on (
                right(roc.object_class, 3) = oc.object_class
                and case when length(roc.object_class) = 4 then left(roc.object_class, 1) = oc.direct_reimbursable when lower(by_direct_reimbursable_funding_source) = 'd' then oc.direct_reimbursable = '1' when lower(by_direct_reimbursable_funding_source) = 'r' then oc.direct_reimbursable = '2' else oc.direct_reimbursable is null end
            )
            where
                fa1.financial_accounts_by_program_activity_object_class_id = fa2.financial_accounts_by_program_activity_object_class_id
        )
    '''

    update_program_activity_sql = '''
     update financial_accounts_by_program_activity_object_class
     set program_activity_id = program_activity_code
    '''

    operations = [
        # migrate data
        # because this is a one-time migration, wrote it in SQL rather than
        # spending the extra time to figure this out via ORM
        migrations.RunSQL(update_object_class_sql, migrations.RunSQL.noop),
        migrations.RunSQL(update_program_activity_sql, migrations.RunSQL.noop)
    ]