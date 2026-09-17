# DB2ADMIN.WRKPMPROPRVMAINTANANCE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89455

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `WORKORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 6 | `SCHEDULINGINTERVAL` | INTEGER | NOT NULL |  |  |  |
| 7 | `PLANNEDSCHDDATE` | DATE |  |  |  |  |
| 8 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 9 | `PMBOMCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `PMBOMCODE` | CHAR(15) |  |  |  |  |
| 11 | `PMBOMLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 12 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 14 | `ACTUALDURATION` | DECIMAL(15,5) |  |  |  |  |
| 15 | `MACHINELOCUSERGENGRPTYPECMYCOD` | CHAR(3) |  |  |  |  |
| 16 | `MACHINELOCUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `MACHINELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 18 | `STARTDATE` | TIMESTAMP |  |  |  |  |
| 19 | `MPUSERGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `MPUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 21 | `MPCODE` | CHAR(10) |  |  |  |  |
| 22 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 23 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 25 | `ENDDATE` | TIMESTAMP |  |  |  |  |
| 26 | `ESTIMATEDDURATION` | DECIMAL(11,2) |  |  |  |  |
| 27 | `REALTIMEOFF` | DECIMAL(11,2) |  |  |  |  |
| 28 | `LABOURCOST` | DECIMAL(18,5) |  |  |  |  |
| 29 | `MATERIALCOST` | DECIMAL(18,5) |  |  |  |  |
| 30 | `SCHEDULINGTYPE` | INTEGER | NOT NULL |  |  |  |
| 31 | `ACTIVITYDESC` | VARCHAR(1000) |  |  |  |  |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPMPROPRVMAINTANANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WORKCENTERCODE,
       t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.WORKORDERCODE,
       t.STATUS,
       t.SCHEDULINGINTERVAL,
       t.PLANNEDSCHDDATE,
       t.LONGDESCRIPTION,
       t.PMBOMCOUNTERCODE,
       t.PMBOMCODE,
       t.PMBOMLONGDESCRIPTION
FROM   DB2ADMIN.WRKPMPROPRVMAINTANANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
