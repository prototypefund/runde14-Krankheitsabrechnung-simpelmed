-- ==============================================================
-- GNUmed database schema change script
--
-- License: GPL v2 or later
-- Author: Karsten Hilbert
-- 
-- ==============================================================
-- $Id: v12-clin-v_health_issues_journal.sql,v 1.1 2009-09-01 22:12:47 ncq Exp $
-- $Revision: 1.1 $

-- --------------------------------------------------------------
\set ON_ERROR_STOP 1

-- --------------------------------------------------------------
\unset ON_ERROR_STOP
drop view clin.v_health_issues_journal cascade;
\set ON_ERROR_STOP 1


create view clin.v_health_issues_journal as
select
	(select fk_patient from clin.encounter where pk = chi.fk_encounter)
		as pk_patient,
	chi.modified_when
		as modified_when,
	coalesce (
		(select dem.identity.dob + chi.age_noted
		 from dem.identity
		 where pk = (select fk_patient from clin.encounter where pk = chi.fk_encounter)
		),
		(select clin.encounter.started from clin.encounter where pk = chi.fk_encounter)
	)
		as clin_when,
	coalesce (
		(select short_alias from dem.staff where db_user = chi.modified_by),
		'<' || chi.modified_by || '>'
	) 	as modified_by,
	'a'::text
		as soap_cat,
	_('Health Issue') || coalesce((' (' || chi.diagnostic_certainty_classification || ')'), '') || ': '
		|| chi.description
		|| coalesce((' (' || chi.laterality || ')'), '') || E'\n '
		|| coalesce(_('noted at age') || ': ' || chi.age_noted::text || E'\n ', '')
		|| case when chi.is_active
			then _('active')
			else _('inactive')
			end
		|| ' / '
		|| case when chi.clinically_relevant
			then _('clinically relevant')
			else _('clinically not relevant')
			end
		|| case when chi.is_confidential
			then ' / ' || _('confidential')
			else ''
			end
		|| case when chi.is_cause_of_death
			then ' / ' || _('cause of death')
			else ''
			end
		as narrative,
	chi.fk_encounter
		as pk_encounter,
	-1
		as pk_episode,
	chi.pk
		as pk_health_issue,
	chi.pk
		as src_pk,
	'clin.health_issue'::text
		as src_table,
	chi.row_version
from
	clin.health_issue chi
;


grant select on clin.v_health_issues_journal TO GROUP "gm-doctors";
-- --------------------------------------------------------------
select gm.log_script_insertion('$RCSfile: v12-clin-v_health_issues_journal.sql,v $', '$Revision: 1.1 $');

-- ==============================================================
-- $Log: v12-clin-v_health_issues_journal.sql,v $
-- Revision 1.1  2009-09-01 22:12:47  ncq
-- - new
--
--