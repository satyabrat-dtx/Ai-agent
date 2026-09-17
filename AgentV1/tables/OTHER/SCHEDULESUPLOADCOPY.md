# DB2ADMIN.SCHEDULESUPLOADCOPY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`, `STEPNUMBER`, `SUBSTEP`, `REPROCESS`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 79017

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `STEPNUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 4 | `SUBSTEP` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `REPROCESS` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `ENVIRONMENTCODE` | CHAR(3) |  |  |  |  |
| 7 | `CANGROUP` | CHAR(2) |  |  |  |  |
| 8 | `GROUPNUMBER` | CHAR(15) |  |  |  |  |
| 9 | `SCHEDULETYPE` | CHAR(2) |  |  |  |  |
| 10 | `SCHEDULEDWORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 11 | `SCHEDULEDRESOURCECODE` | CHAR(8) |  |  |  |  |
| 12 | `SCHEDULEDRESOURCESUBLINE` | INTEGER | NOT NULL |  |  |  |
| 13 | `NUMBEROFRESOURCECOMPONENTS` | INTEGER | NOT NULL |  |  |  |
| 14 | `QUANTITYINPRIMARYUOM` | DECIMAL(15,5) |  |  |  |  |
| 15 | `PRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 16 | `SETUPTIMEBEFOREMATERIAL` | DECIMAL(11,2) |  |  |  |  |
| 17 | `SETUPTIMEAFTERMATERIAL` | DECIMAL(11,2) |  |  |  |  |
| 18 | `EXECUTIONTIME` | DECIMAL(10,5) |  |  |  |  |
| 19 | `INITIALSCHEDULEDDATE` | DATE |  |  |  |  |
| 20 | `INITIALSCHEDULEDTIME` | TIME |  |  |  |  |
| 21 | `FINALSCHEDULEDDATE` | DATE |  |  |  |  |
| 22 | `FINALSCHEDULEDTIME` | TIME |  |  |  |  |
| 23 | `PLANNERCOMMENT` | CHAR(30) |  |  |  |  |
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

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

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
FROM   DB2ADMIN.SCHEDULESUPLOADCOPY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
