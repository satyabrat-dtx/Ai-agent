# DB2ADMIN.WRKWORKCENTERANALYSISDETAIL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 73140

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `STARTINGDATE` | DATE |  |  |  |  |
| 2 | `ENDINGDATE` | DATE |  |  |  |  |
| 3 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 4 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 5 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `PERPERIODIZEDCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 8 | `PERIODPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 9 | `PERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `ANALYSISTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `STEPPRODEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 12 | `STEPPRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 13 | `STEPSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 14 | `TOTALHOURS` | DECIMAL(15,5) |  |  |  |  |
| 15 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 16 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 17 | `CALCULATEDTIME1` | DECIMAL(10,5) |  |  |  |  |
| 18 | `CALCULATEDTIME2` | DECIMAL(10,5) |  |  |  |  |
| 19 | `CALCULATEDTIME3` | DECIMAL(10,5) |  |  |  |  |
| 20 | `CALCULATEDTIME4` | DECIMAL(10,5) |  |  |  |  |
| 21 | `STDBEGINQUEUE` | DATE |  |  |  |  |
| 22 | `STDENDSTEP` | DATE |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

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
       t.STEPPRODEMANDCOUNTERCODE
FROM   DB2ADMIN.WRKWORKCENTERANALYSISDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
