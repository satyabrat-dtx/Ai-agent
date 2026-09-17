# DB2ADMIN.WRKWORKCENTERCAPACITY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 77976

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 1 | `BASEPRIMARYUOM2CODE` | CHAR(3) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `PRIMARYQTYPLANNED` | DECIMAL(15,5) |  |  |  |  |
| 4 | `PRIMARYQTYPROCESS` | DECIMAL(15,5) |  |  |  |  |
| 5 | `PRIMARYQTY2PLANNED` | DECIMAL(15,5) |  |  |  |  |
| 6 | `PRIMARYQTY2PROCESS` | DECIMAL(15,5) |  |  |  |  |
| 7 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 8 | `BASESECONDARYUOM2CODE` | CHAR(3) |  |  |  |  |
| 9 | `SECONDARYQTYPLANNED` | DECIMAL(15,5) |  |  |  |  |
| 10 | `SECONDARYQTY2PLANNED` | DECIMAL(15,5) |  |  |  |  |
| 11 | `SECONDARYQTYPROCESS` | DECIMAL(15,5) |  |  |  |  |
| 12 | `SECONDARYQTY2PROCESS` | DECIMAL(15,5) |  |  |  |  |
| 13 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 16 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 17 | `WORKCENTERDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 18 | `PERPERIODIZEDCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 19 | `PERIODPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 20 | `PERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 21 | `ANALYSISTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 22 | `TOTALHOURS` | DECIMAL(15,5) |  |  |  |  |
| 23 | `TOTALPERCENT` | DECIMAL(15,5) |  |  |  |  |
| 24 | `PLANNEDQUEUETIME` | DECIMAL(15,5) |  |  |  |  |
| 25 | `PROGRESSQUEUETIME` | DECIMAL(15,5) |  |  |  |  |
| 26 | `PLANNEDPREPROCESSTIME` | DECIMAL(15,5) |  |  |  |  |
| 27 | `PLANNEDPROCESSTIME` | DECIMAL(15,5) |  |  |  |  |
| 28 | `PROGRESSPROCESSTIME` | DECIMAL(15,5) |  |  |  |  |
| 29 | `PLANNEDPOSTPROCESSTIME` | DECIMAL(15,5) |  |  |  |  |
| 30 | `PROGRESSPOSTPROCESSTIME` | DECIMAL(15,5) |  |  |  |  |
| 31 | `PLANNEDREOPERATIONTIME` | DECIMAL(15,5) |  |  |  |  |
| 32 | `PROGRESSREOPERATIONTIME` | DECIMAL(15,5) |  |  |  |  |
| 33 | `PROGRESSPREPROCESSTIME` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.BASEPRIMARYUOMCODE,
       t.BASEPRIMARYUOM2CODE,
       t.COMPANYCODE,
       t.PRIMARYQTYPLANNED,
       t.PRIMARYQTYPROCESS,
       t.PRIMARYQTY2PLANNED,
       t.PRIMARYQTY2PROCESS,
       t.BASESECONDARYUOMCODE,
       t.BASESECONDARYUOM2CODE,
       t.SECONDARYQTYPLANNED,
       t.SECONDARYQTY2PLANNED,
       t.SECONDARYQTYPROCESS
FROM   DB2ADMIN.WRKWORKCENTERCAPACITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
