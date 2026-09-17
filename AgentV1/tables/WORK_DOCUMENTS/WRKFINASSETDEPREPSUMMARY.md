# DB2ADMIN.WRKFINASSETDEPREPSUMMARY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178180

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(10) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 5 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 6 | `MAINASSETCODE` | CHAR(10) |  |  |  |  |
| 7 | `MAINASSETDESC` | VARCHAR(200) |  |  |  |  |
| 8 | `ASSTGROUP` | CHAR(10) |  |  |  |  |
| 9 | `GROUPDESC` | VARCHAR(200) |  |  |  |  |
| 10 | `ASSTCODE` | CHAR(15) |  |  |  |  |
| 11 | `ASSETDESC` | VARCHAR(200) |  |  |  |  |
| 12 | `TOTALDEP` | DECIMAL(18,5) |  |  |  |  |
| 13 | `JAN` | DECIMAL(18,5) |  |  |  |  |
| 14 | `FEB` | DECIMAL(18,5) |  |  |  |  |
| 15 | `MAR` | DECIMAL(18,5) |  |  |  |  |
| 16 | `APR` | DECIMAL(18,5) |  |  |  |  |
| 17 | `MAY` | DECIMAL(18,5) |  |  |  |  |
| 18 | `JUN` | DECIMAL(18,5) |  |  |  |  |
| 19 | `JUL` | DECIMAL(18,5) |  |  |  |  |
| 20 | `AUG` | DECIMAL(18,5) |  |  |  |  |
| 21 | `SEP` | DECIMAL(18,5) |  |  |  |  |
| 22 | `OCT` | DECIMAL(18,5) |  |  |  |  |
| 23 | `NOV` | DECIMAL(18,5) |  |  |  |  |
| 24 | `DEC` | DECIMAL(18,5) |  |  |  |  |
| 25 | `POSTINGDATE` | DATE |  |  |  |  |
| 26 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.PROFITCENTERCODE,
       t.MAINASSETCODE,
       t.MAINASSETDESC,
       t.ASSTGROUP,
       t.GROUPDESC,
       t.ASSTCODE,
       t.ASSETDESC
FROM   DB2ADMIN.WRKFINASSETDEPREPSUMMARY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
