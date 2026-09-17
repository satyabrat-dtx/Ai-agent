# DB2ADMIN.WRKPMCORRECTIVETIME

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89379

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `WORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `WORKORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 6 | `WORKORDERDATE` | DATE |  |  |  |  |
| 7 | `STATUS` | CHAR(20) |  |  |  |  |
| 8 | `SYMPTOM` | VARCHAR(1000) |  |  |  |  |
| 9 | `TIMEPLANNING` | TIMESTAMP |  |  |  |  |
| 10 | `TIMEPLANNINGHOURS` | DECIMAL(15,5) |  |  |  |  |
| 11 | `TIMEALLOCATION` | DECIMAL(15,5) |  |  |  |  |
| 12 | `RUNTIME` | DECIMAL(15,5) |  |  |  |  |
| 13 | `TOTALRESPONSETIME` | DECIMAL(15,5) |  |  |  |  |
| 14 | `ORDERCOMMENTS` | VARCHAR(1000) |  |  |  |  |
| 15 | `WORKORDERENDDATE` | TIMESTAMP |  |  |  |  |
| 16 | `PMBOMCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 17 | `PMBOMCODE` | CHAR(15) |  |  |  |  |
| 18 | `MACHINEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 19 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 20 | `COSTCENTERDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 21 | `WORKPLACE` | CHAR(15) |  |  |  |  |
| 22 | `PLANNINGGROUP` | CHAR(15) |  |  |  |  |
| 23 | `PRIORITY` | CHAR(10) |  |  |  |  |
| 24 | `AUXILIARYHOURS` | DECIMAL(15,5) |  |  |  |  |
| 25 | `ADMINHOURS` | DECIMAL(15,5) |  |  |  |  |
| 26 | `ASSISTANTHOURS` | DECIMAL(15,5) |  |  |  |  |
| 27 | `ELECTRICALHOURS` | DECIMAL(15,5) |  |  |  |  |
| 28 | `ELECTRICIANHOURS` | DECIMAL(15,5) |  |  |  |  |
| 29 | `INSTRUMENTHOURS` | DECIMAL(15,5) |  |  |  |  |
| 30 | `MECHANICALHOURS` | DECIMAL(15,5) |  |  |  |  |
| 31 | `MECHANICALCALDHOURS` | DECIMAL(15,5) |  |  |  |  |
| 32 | `MAINTENANCEHOURS` | DECIMAL(15,5) |  |  |  |  |
| 33 | `OPERATORHOURS` | DECIMAL(15,5) |  |  |  |  |
| 34 | `BOILERHOURS` | DECIMAL(15,5) |  |  |  |  |
| 35 | `MAINSUPERHOURS` | DECIMAL(15,5) |  |  |  |  |
| 36 | `MILLINGHOURS` | DECIMAL(15,5) |  |  |  |  |
| 37 | `ACTIVITYCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 38 | `ACTIVITYCODE` | CHAR(15) |  |  |  |  |
| 39 | `ACTIVITYDESCRIPTION` | VARCHAR(1000) |  |  |  |  |
| 40 | `ACTIVITYREMARKS` | VARCHAR(1000) |  |  |  |  |
| 41 | `LABOURCOST` | DECIMAL(15,5) |  |  |  |  |
| 42 | `MATERIALCOST` | DECIMAL(15,5) |  |  |  |  |
| 43 | `ACTUALCOST` | DECIMAL(15,5) |  |  |  |  |
| 44 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPMCORRECTIVETIMEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.WORKORDERCOUNTERCODE,
       t.WORKORDERCODE,
       t.PLANTCODE,
       t.WORKORDERDATE,
       t.STATUS,
       t.SYMPTOM,
       t.TIMEPLANNING,
       t.TIMEPLANNINGHOURS,
       t.TIMEALLOCATION
FROM   DB2ADMIN.WRKPMCORRECTIVETIME t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
