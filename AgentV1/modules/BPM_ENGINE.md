# Module: BPM_ENGINE

Activiti/Flowable business-process-engine tables (ACT_* prefix). Engine-internal runtime, history and identity state. Not application business data.

- **Tables**: 79
- **Label basis**: table-name prefix matching
- **Per-table confidence**: {'high': 79}

## Most-referenced tables in this module

| Table | Inbound FKs | Columns | Primary key |
|---|---|---|---|
| [`ACT_RU_EXECUTION`](../tables/BPM_ENGINE/ACT_RU_EXECUTION.md) | 17 | 39 | ID_ |
| [`ACT_GE_BYTEARRAY`](../tables/BPM_ENGINE/ACT_GE_BYTEARRAY.md) | 14 | 6 | ID_ |
| [`ACT_RE_PROCDEF`](../tables/BPM_ENGINE/ACT_RE_PROCDEF.md) | 8 | 18 | ID_ |
| [`ACT_CMMN_CASEDEF`](../tables/BPM_ENGINE/ACT_CMMN_CASEDEF.md) | 4 | 13 | ID_ |
| [`ACT_CMMN_RU_CASE_INST`](../tables/BPM_ENGINE/ACT_CMMN_RU_CASE_INST.md) | 3 | 20 | ID_ |
| [`ACT_RE_DEPLOYMENT`](../tables/BPM_ENGINE/ACT_RE_DEPLOYMENT.md) | 2 | 10 | ID_ |
| [`ACT_CMMN_DEPLOYMENT`](../tables/BPM_ENGINE/ACT_CMMN_DEPLOYMENT.md) | 2 | 7 | ID_ |
| [`ACT_APP_DEPLOYMENT`](../tables/BPM_ENGINE/ACT_APP_DEPLOYMENT.md) | 2 | 6 | ID_ |
| [`ACT_DE_MODEL`](../tables/BPM_ENGINE/ACT_DE_MODEL.md) | 2 | 14 | ID |
| [`ACT_RU_TASK`](../tables/BPM_ENGINE/ACT_RU_TASK.md) | 1 | 30 | ID_ |
| [`ACT_ID_GROUP`](../tables/BPM_ENGINE/ACT_ID_GROUP.md) | 1 | 4 | ID_ |
| [`ACT_ID_USER`](../tables/BPM_ENGINE/ACT_ID_USER.md) | 1 | 9 | ID_ |
| [`ACT_ID_PRIV`](../tables/BPM_ENGINE/ACT_ID_PRIV.md) | 1 | 2 | ID_ |
| [`ACT_CMMN_RU_PLAN_ITEM_INST`](../tables/BPM_ENGINE/ACT_CMMN_RU_PLAN_ITEM_INST.md) | 1 | 35 | ID_ |
| [`ACT_GE_PROPERTY`](../tables/BPM_ENGINE/ACT_GE_PROPERTY.md) | 0 | 3 | NAME_ |

## All tables

- [`ACT_ADM_DATABASECHANGELOG`](../tables/BPM_ENGINE/ACT_ADM_DATABASECHANGELOG.md) — 14 cols  ⛔ not for business queries
- [`ACT_ADM_DATABASECHANGELOGLOCK`](../tables/BPM_ENGINE/ACT_ADM_DATABASECHANGELOGLOCK.md) — 4 cols  ⛔ not for business queries
- [`ACT_ADM_SERVER_CONFIG`](../tables/BPM_ENGINE/ACT_ADM_SERVER_CONFIG.md) — 11 cols  ⛔ not for business queries
- [`ACT_APP_APPDEF`](../tables/BPM_ENGINE/ACT_APP_APPDEF.md) — 10 cols  ⛔ not for business queries
- [`ACT_APP_DATABASECHANGELOG`](../tables/BPM_ENGINE/ACT_APP_DATABASECHANGELOG.md) — 14 cols  ⛔ not for business queries
- [`ACT_APP_DATABASECHANGELOGLOCK`](../tables/BPM_ENGINE/ACT_APP_DATABASECHANGELOGLOCK.md) — 4 cols  ⛔ not for business queries
- [`ACT_APP_DEPLOYMENT`](../tables/BPM_ENGINE/ACT_APP_DEPLOYMENT.md) — 6 cols  ⛔ not for business queries
- [`ACT_APP_DEPLOYMENT_RESOURCE`](../tables/BPM_ENGINE/ACT_APP_DEPLOYMENT_RESOURCE.md) — 4 cols  ⛔ not for business queries
- [`ACT_CMMN_CASEDEF`](../tables/BPM_ENGINE/ACT_CMMN_CASEDEF.md) — 13 cols  ⛔ not for business queries
- [`ACT_CMMN_DATABASECHANGELOG`](../tables/BPM_ENGINE/ACT_CMMN_DATABASECHANGELOG.md) — 14 cols  ⛔ not for business queries
- [`ACT_CMMN_DATABASECHANGELOGLOCK`](../tables/BPM_ENGINE/ACT_CMMN_DATABASECHANGELOGLOCK.md) — 4 cols  ⛔ not for business queries
- [`ACT_CMMN_DEPLOYMENT`](../tables/BPM_ENGINE/ACT_CMMN_DEPLOYMENT.md) — 7 cols  ⛔ not for business queries
- [`ACT_CMMN_DEPLOYMENT_RESOURCE`](../tables/BPM_ENGINE/ACT_CMMN_DEPLOYMENT_RESOURCE.md) — 5 cols  ⛔ not for business queries
- [`ACT_CMMN_HI_CASE_INST`](../tables/BPM_ENGINE/ACT_CMMN_HI_CASE_INST.md) — 18 cols  ⛔ not for business queries
- [`ACT_CMMN_HI_MIL_INST`](../tables/BPM_ENGINE/ACT_CMMN_HI_MIL_INST.md) — 8 cols  ⛔ not for business queries
- [`ACT_CMMN_HI_PLAN_ITEM_INST`](../tables/BPM_ENGINE/ACT_CMMN_HI_PLAN_ITEM_INST.md) — 33 cols  ⛔ not for business queries
- [`ACT_CMMN_RU_CASE_INST`](../tables/BPM_ENGINE/ACT_CMMN_RU_CASE_INST.md) — 20 cols  ⛔ not for business queries
- [`ACT_CMMN_RU_MIL_INST`](../tables/BPM_ENGINE/ACT_CMMN_RU_MIL_INST.md) — 7 cols  ⛔ not for business queries
- [`ACT_CMMN_RU_PLAN_ITEM_INST`](../tables/BPM_ENGINE/ACT_CMMN_RU_PLAN_ITEM_INST.md) — 35 cols  ⛔ not for business queries
- [`ACT_CMMN_RU_SENTRY_PART_INST`](../tables/BPM_ENGINE/ACT_CMMN_RU_SENTRY_PART_INST.md) — 8 cols  ⛔ not for business queries
- [`ACT_CO_CONTENT_ITEM`](../tables/BPM_ENGINE/ACT_CO_CONTENT_ITEM.md) — 17 cols  ⛔ not for business queries
- [`ACT_CO_DATABASECHANGELOG`](../tables/BPM_ENGINE/ACT_CO_DATABASECHANGELOG.md) — 14 cols  ⛔ not for business queries
- [`ACT_CO_DATABASECHANGELOGLOCK`](../tables/BPM_ENGINE/ACT_CO_DATABASECHANGELOGLOCK.md) — 4 cols  ⛔ not for business queries
- [`ACT_DE_DATABASECHANGELOG`](../tables/BPM_ENGINE/ACT_DE_DATABASECHANGELOG.md) — 14 cols  ⛔ not for business queries
- [`ACT_DE_DATABASECHANGELOGLOCK`](../tables/BPM_ENGINE/ACT_DE_DATABASECHANGELOGLOCK.md) — 4 cols  ⛔ not for business queries
- [`ACT_DE_MODEL`](../tables/BPM_ENGINE/ACT_DE_MODEL.md) — 14 cols  ⛔ not for business queries
- [`ACT_DE_MODEL_HISTORY`](../tables/BPM_ENGINE/ACT_DE_MODEL_HISTORY.md) — 15 cols  ⛔ not for business queries
- [`ACT_DE_MODEL_RELATION`](../tables/BPM_ENGINE/ACT_DE_MODEL_RELATION.md) — 4 cols  ⛔ not for business queries
- [`ACT_DMN_DATABASECHANGELOG`](../tables/BPM_ENGINE/ACT_DMN_DATABASECHANGELOG.md) — 14 cols  ⛔ not for business queries
- [`ACT_DMN_DATABASECHANGELOGLOCK`](../tables/BPM_ENGINE/ACT_DMN_DATABASECHANGELOGLOCK.md) — 4 cols  ⛔ not for business queries
- [`ACT_DMN_DECISION`](../tables/BPM_ENGINE/ACT_DMN_DECISION.md) — 10 cols  ⛔ not for business queries
- [`ACT_DMN_DEPLOYMENT`](../tables/BPM_ENGINE/ACT_DMN_DEPLOYMENT.md) — 6 cols  ⛔ not for business queries
- [`ACT_DMN_DEPLOYMENT_RESOURCE`](../tables/BPM_ENGINE/ACT_DMN_DEPLOYMENT_RESOURCE.md) — 4 cols  ⛔ not for business queries
- [`ACT_DMN_HI_DECISION_EXECUTION`](../tables/BPM_ENGINE/ACT_DMN_HI_DECISION_EXECUTION.md) — 12 cols  ⛔ not for business queries
- [`ACT_EVT_LOG`](../tables/BPM_ENGINE/ACT_EVT_LOG.md) — 12 cols  ⛔ not for business queries
- [`ACT_FO_DATABASECHANGELOG`](../tables/BPM_ENGINE/ACT_FO_DATABASECHANGELOG.md) — 14 cols  ⛔ not for business queries
- [`ACT_FO_DATABASECHANGELOGLOCK`](../tables/BPM_ENGINE/ACT_FO_DATABASECHANGELOGLOCK.md) — 4 cols  ⛔ not for business queries
- [`ACT_FO_FORM_DEFINITION`](../tables/BPM_ENGINE/ACT_FO_FORM_DEFINITION.md) — 9 cols  ⛔ not for business queries
- [`ACT_FO_FORM_DEPLOYMENT`](../tables/BPM_ENGINE/ACT_FO_FORM_DEPLOYMENT.md) — 6 cols  ⛔ not for business queries
- [`ACT_FO_FORM_INSTANCE`](../tables/BPM_ENGINE/ACT_FO_FORM_INSTANCE.md) — 12 cols  ⛔ not for business queries
- [`ACT_FO_FORM_RESOURCE`](../tables/BPM_ENGINE/ACT_FO_FORM_RESOURCE.md) — 4 cols  ⛔ not for business queries
- [`ACT_GE_BYTEARRAY`](../tables/BPM_ENGINE/ACT_GE_BYTEARRAY.md) — 6 cols  ⛔ not for business queries
- [`ACT_GE_PROPERTY`](../tables/BPM_ENGINE/ACT_GE_PROPERTY.md) — 3 cols  ⛔ not for business queries
- [`ACT_HI_ACTINST`](../tables/BPM_ENGINE/ACT_HI_ACTINST.md) — 18 cols  ⛔ not for business queries
- [`ACT_HI_ATTACHMENT`](../tables/BPM_ENGINE/ACT_HI_ATTACHMENT.md) — 11 cols  ⛔ not for business queries
- [`ACT_HI_COMMENT`](../tables/BPM_ENGINE/ACT_HI_COMMENT.md) — 9 cols  ⛔ not for business queries
- [`ACT_HI_DETAIL`](../tables/BPM_ENGINE/ACT_HI_DETAIL.md) — 15 cols  ⛔ not for business queries
- [`ACT_HI_ENTITYLINK`](../tables/BPM_ENGINE/ACT_HI_ENTITYLINK.md) — 14 cols  ⛔ not for business queries
- [`ACT_HI_IDENTITYLINK`](../tables/BPM_ENGINE/ACT_HI_IDENTITYLINK.md) — 11 cols  ⛔ not for business queries
- [`ACT_HI_PROCINST`](../tables/BPM_ENGINE/ACT_HI_PROCINST.md) — 21 cols  ⛔ not for business queries
- [`ACT_HI_TASKINST`](../tables/BPM_ENGINE/ACT_HI_TASKINST.md) — 28 cols  ⛔ not for business queries
- [`ACT_HI_TSK_LOG`](../tables/BPM_ENGINE/ACT_HI_TSK_LOG.md) — 14 cols  ⛔ not for business queries
- [`ACT_HI_VARINST`](../tables/BPM_ENGINE/ACT_HI_VARINST.md) — 17 cols  ⛔ not for business queries
- [`ACT_ID_BYTEARRAY`](../tables/BPM_ENGINE/ACT_ID_BYTEARRAY.md) — 4 cols  ⛔ not for business queries
- [`ACT_ID_GROUP`](../tables/BPM_ENGINE/ACT_ID_GROUP.md) — 4 cols  ⛔ not for business queries
- [`ACT_ID_INFO`](../tables/BPM_ENGINE/ACT_ID_INFO.md) — 8 cols  ⛔ not for business queries
- [`ACT_ID_MEMBERSHIP`](../tables/BPM_ENGINE/ACT_ID_MEMBERSHIP.md) — 2 cols  ⛔ not for business queries
- [`ACT_ID_PRIV`](../tables/BPM_ENGINE/ACT_ID_PRIV.md) — 2 cols  ⛔ not for business queries
- [`ACT_ID_PRIV_MAPPING`](../tables/BPM_ENGINE/ACT_ID_PRIV_MAPPING.md) — 4 cols  ⛔ not for business queries
- [`ACT_ID_PROPERTY`](../tables/BPM_ENGINE/ACT_ID_PROPERTY.md) — 3 cols  ⛔ not for business queries
- [`ACT_ID_TOKEN`](../tables/BPM_ENGINE/ACT_ID_TOKEN.md) — 8 cols  ⛔ not for business queries
- [`ACT_ID_USER`](../tables/BPM_ENGINE/ACT_ID_USER.md) — 9 cols  ⛔ not for business queries
- [`ACT_PROCDEF_INFO`](../tables/BPM_ENGINE/ACT_PROCDEF_INFO.md) — 4 cols  ⛔ not for business queries
- [`ACT_RE_DEPLOYMENT`](../tables/BPM_ENGINE/ACT_RE_DEPLOYMENT.md) — 10 cols  ⛔ not for business queries
- [`ACT_RE_MODEL`](../tables/BPM_ENGINE/ACT_RE_MODEL.md) — 13 cols  ⛔ not for business queries
- [`ACT_RE_PROCDEF`](../tables/BPM_ENGINE/ACT_RE_PROCDEF.md) — 18 cols  ⛔ not for business queries
- [`ACT_RU_ACTINST`](../tables/BPM_ENGINE/ACT_RU_ACTINST.md) — 17 cols  ⛔ not for business queries
- [`ACT_RU_DEADLETTER_JOB`](../tables/BPM_ENGINE/ACT_RU_DEADLETTER_JOB.md) — 24 cols  ⛔ not for business queries
- [`ACT_RU_ENTITYLINK`](../tables/BPM_ENGINE/ACT_RU_ENTITYLINK.md) — 15 cols  ⛔ not for business queries
- [`ACT_RU_EVENT_SUBSCR`](../tables/BPM_ENGINE/ACT_RU_EVENT_SUBSCR.md) — 17 cols  ⛔ not for business queries
- [`ACT_RU_EXECUTION`](../tables/BPM_ENGINE/ACT_RU_EXECUTION.md) — 39 cols  ⛔ not for business queries
- [`ACT_RU_EXTERNAL_JOB`](../tables/BPM_ENGINE/ACT_RU_EXTERNAL_JOB.md) — 27 cols  ⛔ not for business queries
- [`ACT_RU_HISTORY_JOB`](../tables/BPM_ENGINE/ACT_RU_HISTORY_JOB.md) — 14 cols  ⛔ not for business queries
- [`ACT_RU_IDENTITYLINK`](../tables/BPM_ENGINE/ACT_RU_IDENTITYLINK.md) — 12 cols  ⛔ not for business queries
- [`ACT_RU_JOB`](../tables/BPM_ENGINE/ACT_RU_JOB.md) — 27 cols  ⛔ not for business queries
- [`ACT_RU_SUSPENDED_JOB`](../tables/BPM_ENGINE/ACT_RU_SUSPENDED_JOB.md) — 25 cols  ⛔ not for business queries
- [`ACT_RU_TASK`](../tables/BPM_ENGINE/ACT_RU_TASK.md) — 30 cols  ⛔ not for business queries
- [`ACT_RU_TIMER_JOB`](../tables/BPM_ENGINE/ACT_RU_TIMER_JOB.md) — 27 cols  ⛔ not for business queries
- [`ACT_RU_VARIABLE`](../tables/BPM_ENGINE/ACT_RU_VARIABLE.md) — 15 cols  ⛔ not for business queries