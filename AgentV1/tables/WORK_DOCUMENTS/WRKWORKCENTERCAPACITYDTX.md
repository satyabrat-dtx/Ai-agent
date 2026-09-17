# DB2ADMIN.WRKWORKCENTERCAPACITYDTX

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 72442

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `STARTINGDATE` | DATE |  |  |  |  |
| 2 | `ENDINGDATE` | DATE |  |  |  |  |
| 3 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 4 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 5 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `PERPERIODIZEDCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 8 | `PERIODPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 9 | `PERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `ANALYSISTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `TOTALHOURS` | DECIMAL(11,5) |  |  |  |  |
| 12 | `STEPPRODEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `STEPPRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 14 | `STEPSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKWORKCENTERCAPACITYDTXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.STARTINGDATE,
       t.ENDINGDATE,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.WORKCENTERCODE,
       t.PERPERIODIZEDCALENDARTYPECODE,
       t.PERIODPERIODIZEDCALENDARYEAR,
       t.PERIODCODE,
       t.ANALYSISTYPE,
       t.TOTALHOURS
FROM   DB2ADMIN.WRKWORKCENTERCAPACITYDTX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
