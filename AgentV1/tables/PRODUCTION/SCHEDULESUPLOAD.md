# DB2ADMIN.SCHEDULESUPLOAD

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 43
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`, `STEPNUMBER`, `SUBSTEP`, `REPROCESS`, `HIGHLEVELSCHEDULE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70161

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `STEPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 4 | `SUBSTEP` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `REPROCESS` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `ENVIRONMENTCODE` | CHAR(3) |  |  |  |  |
| 7 | `CANGROUP` | CHAR(2) |  |  |  |  |
| 8 | `GROUPNUMBER` | CHAR(15) |  |  |  |  |
| 9 | `SCHEDULETYPE` | CHAR(2) |  |  |  |  |
| 10 | `SCHEDULEDWORKCENTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 11 | `SCHEDULEDRESOURCECODE` | CHAR(8) |  | FK | foreign_key |  |
| 12 | `SCHEDULEDRESOURCESUBLINE` | INTEGER | NOT NULL |  |  |  |
| 13 | `NUMBEROFRESOURCECOMPONENTS` | INTEGER | NOT NULL |  |  |  |
| 14 | `QUANTITYINPRIMARYUOM` | DECIMAL(15,5) |  |  |  |  |
| 15 | `PRIMARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `SETUPTIMEBEFOREMATERIAL` | DECIMAL(11,2) |  |  |  |  |
| 17 | `SETUPTIMEAFTERMATERIAL` | DECIMAL(11,2) |  |  |  |  |
| 18 | `EXECUTIONTIME` | DECIMAL(15,5) |  |  |  |  |
| 19 | `INITIALSCHEDULEDDATE` | DATE |  |  |  |  |
| 20 | `INITIALSCHEDULEDTIME` | TIME |  |  |  |  |
| 21 | `FINALSCHEDULEDDATE` | DATE |  |  |  |  |
| 22 | `FINALSCHEDULEDTIME` | TIME |  |  |  |  |
| 23 | `PLANNERCOMMENT` | CHAR(120) |  |  |  |  |
| 24 | `NEWDEMANDUNIQUEID` | CHAR(10) |  |  |  |  |
| 25 | `SPLITFAMILY` | CHAR(12) |  |  |  |  |
| 26 | `CHANGETYPE` | CHAR(2) |  |  |  |  |
| 27 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 28 | `PROCESSCODE` | CHAR(2) |  |  |  |  |
| 29 | `PROCESSDESCRIPTION` | CHAR(30) |  |  |  |  |
| 30 | `CREATEDDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 31 | `PRODUCTIONORDERCREATED` | CHAR(15) |  |  |  |  |
| 32 | `CREATEDDEMANDCODE` | CHAR(15) |  |  |  |  |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 34 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 35 | `HIGHLEVELSCHEDULE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 36 | `INITIALSCHEDULEDACTUALDATE` | DATE |  |  |  |  |
| 37 | `INITIALSCHEDULEDACTUALTIME` | TIME |  |  |  |  |
| 38 | `FINALSCHEDULEDACTUALDATE` | DATE |  |  |  |  |
| 39 | `FINALSCHEDULEDACTUALTIME` | TIME |  |  |  |  |
| 40 | `THREADOPERATION` | CHAR(2) |  |  |  |  |
| 41 | `THREADLOCKNUMBER` | DECIMAL(7,0) |  |  |  |  |
| 42 | `THREADSTATUS` | CHAR(2) |  |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SCHEDULESUPLOAD.COMPANYCODE = COMPANY.CODE` |
| `RESOURCES_SCHEDULEDRESOURCE` | `COMPANYCODE`, `SCHEDULEDRESOURCECODE` | [`RESOURCES`](../PRODUCTION/RESOURCES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCHEDULESUPLOAD.COMPANYCODE = RESOURCES.COMPANYCODE AND SCHEDULESUPLOAD.SCHEDULEDRESOURCECODE = RESOURCES.CODE` |
| `UNITOFMEASURE_PRIMARYUOM` | `PRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `SCHEDULESUPLOAD.PRIMARYUOMCODE = UNITOFMEASURE.CODE` |
| `WORKCENTER_SCHEDULEDWORKCENTER` | `COMPANYCODE`, `SCHEDULEDWORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCHEDULESUPLOAD.COMPANYCODE = WORKCENTER.COMPANYCODE AND SCHEDULESUPLOAD.SCHEDULEDWORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SCHEDULESUPLOADUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.STEPNUMBER,
       t.SUBSTEP,
       t.REPROCESS,
       t.ENVIRONMENTCODE,
       t.CANGROUP,
       t.GROUPNUMBER,
       t.SCHEDULETYPE,
       t.SCHEDULEDWORKCENTERCODE,
       t.SCHEDULEDRESOURCECODE
FROM   DB2ADMIN.SCHEDULESUPLOAD t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
