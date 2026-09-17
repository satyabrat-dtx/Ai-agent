# DB2ADMIN.SCHEDULESOFSTEPSPLITS

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 2 of 2 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 39
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`, `STEPNUMBER`, `SUBSTEP`, `REPROCESS`, `HIGHLEVELSCHEDULE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70087

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
| 26 | `CREATEDDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 27 | `PRODUCTIONORDERCREATED` | CHAR(15) |  |  |  |  |
| 28 | `CREATEDDEMANDCODE` | CHAR(15) |  |  |  |  |
| 29 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 30 | `HIGHLEVELSCHEDULE` | SMALLINT | NOT NULL | PK | primary_key |  |
| 31 | `TEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 32 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 33 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 34 | `INITIALSCHEDULEDACTUALDATE` | DATE |  |  |  |  |
| 35 | `INITIALSCHEDULEDACTUALTIME` | TIME |  |  |  |  |
| 36 | `FINALSCHEDULEDACTUALDATE` | DATE |  |  |  |  |
| 37 | `FINALSCHEDULEDACTUALTIME` | TIME |  |  |  |  |
| 38 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SCHEDULESOFSTEPSPLITS.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCHEDULESOFSTEPSPLITS.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND SCHEDULESOFSTEPSPLITS.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `PRODUCTIONDEMANDTEMPLATE_TEMPLATE` | `COMPANYCODE`, `TEMPLATECODE` | [`PRODUCTIONDEMANDTEMPLATE`](../PRODUCTION/PRODUCTIONDEMANDTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCHEDULESOFSTEPSPLITS.COMPANYCODE = PRODUCTIONDEMANDTEMPLATE.COMPANYCODE AND SCHEDULESOFSTEPSPLITS.TEMPLATECODE = PRODUCTIONDEMANDTEMPLATE.CODE` |
| `RESOURCES_SCHEDULEDRESOURCE` | `COMPANYCODE`, `SCHEDULEDRESOURCECODE` | [`RESOURCES`](../PRODUCTION/RESOURCES.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCHEDULESOFSTEPSPLITS.COMPANYCODE = RESOURCES.COMPANYCODE AND SCHEDULESOFSTEPSPLITS.SCHEDULEDRESOURCECODE = RESOURCES.CODE` |
| `UNITOFMEASURE_PRIMARYUOM` | `PRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `SCHEDULESOFSTEPSPLITS.PRIMARYUOMCODE = UNITOFMEASURE.CODE` |
| `WORKCENTER_SCHEDULEDWORKCENTER` | `COMPANYCODE`, `SCHEDULEDWORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SCHEDULESOFSTEPSPLITS.COMPANYCODE = WORKCENTER.COMPANYCODE AND SCHEDULESOFSTEPSPLITS.SCHEDULEDWORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SCHEDULESOFSTEPSPLITSUID` (ABSUNIQUEID)

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
FROM   DB2ADMIN.SCHEDULESOFSTEPSPLITS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
