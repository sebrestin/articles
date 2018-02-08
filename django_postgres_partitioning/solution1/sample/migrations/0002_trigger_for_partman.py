from django.db import migrations

# trigger to remove the duplicate data.
# if the trigger exists, it means that the data was added before to the correct partition.
# the trigger can be missing in case of undoing partitioning(moving data back to the parent).
CREATE_PARTMAN_TRIGGER_FUNC = 'CREATE OR REPLACE FUNCTION trg_func_after_insert() RETURNS trigger AS $func$ '\
                                'DECLARE '\
                                    'v_trigger_exists bool;'\
                                    'v_trig_name text;'\
                                    'v_count int;'\
                                    'v_partition_interval int;'\
                                'BEGIN '\
                                'SELECT partition_interval INTO v_partition_interval FROM partman.part_config;'\
                                'IF v_partition_interval > 0 THEN '\
                                    'v_trig_name := partman.check_name_length(p_object_name := \'sample_sample1\', p_suffix := \'_part_trig\');'\
                                    'v_trigger_exists := EXISTS (SELECT 1 FROM pg_trigger WHERE NOT tgisinternal AND tgname = v_trig_name);'\
                                    'IF v_trigger_exists THEN '\
                                        'DELETE FROM ONLY public.sample_sample1 WHERE id = NEW.id;'\
                                    'END IF;'\
                                'END IF;'\
                                'RETURN NULL;'\
                               'END $func$'\
                               'LANGUAGE plpgsql;'

DROP_PARTMAN_TRIGGER_FUNC = 'DROP FUNCTION IF EXISTS trg_func_after_insert();'

CREATE_PARTMAN_TRIGGER = 'CREATE TRIGGER trg_after_insert AFTER INSERT ON sample_sample1 FOR EACH ROW EXECUTE PROCEDURE trg_func_after_insert();'
DROP_PARTMAN_TRIGGER = 'DROP TRIGGER IF EXISTS trg_after_insert ON sample_sample1;'


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(sql=CREATE_PARTMAN_TRIGGER_FUNC, reverse_sql=DROP_PARTMAN_TRIGGER_FUNC),
        migrations.RunSQL(sql=CREATE_PARTMAN_TRIGGER, reverse_sql=DROP_PARTMAN_TRIGGER)
    ]
