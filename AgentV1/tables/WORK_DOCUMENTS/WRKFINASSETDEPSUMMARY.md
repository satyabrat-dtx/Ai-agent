# DB2ADMIN.WRKFINASSETDEPSUMMARY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178227

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 4 | `COMPANYCODE` | CHAR(10) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 6 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 7 | `MAINASSETCODE` | CHAR(10) |  |  |  |  |
| 8 | `MAINASSETDESC` | VARCHAR(200) |  |  |  |  |
| 9 | `ASSTGROUP` | CHAR(10) |  |  |  |  |
| 10 | `GROUPDESC` | VARCHAR(200) |  |  |  |  |
| 11 | `ASSTCODE` | CHAR(15) |  |  |  |  |
| 12 | `ASSETDESC` | VARCHAR(200) |  |  |  |  |
| 13 | `OPVAL` | DECIMAL(18,5) |  |  |  |  |
| 14 | `PURVAL` | DECIMAL(18,5) |  |  |  |  |
| 15 | `SALEVAL` | DECIMAL(18,5) |  |  |  |  |
| 16 | `NETASSTVAL` | DECIMAL(18,5) |  |  |  |  |
| 17 | `DOPBAL` | DECIMAL(18,5) |  |  |  |  |
| 18 | `DEPVAL` | DECIMAL(18,5) |  |  |  |  |
| 19 | `DEDVAL` | DECIMAL(18,5) |  |  |  |  |
| 20 | `NETASSTVAL1` | DECIMAL(18,5) |  |  |  |  |
| 21 | `NETASSTVAL2` | DECIMAL(18,5) |  |  |  |  |
| 22 | `NETASSTVAL3` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COSTCENTERCODE,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.PROFITCENTERCODE,
       t.MAINASSETCODE,
       t.MAINASSETDESC,
       t.ASSTGROUP,
       t.GROUPDESC,
       t.ASSTCODE
FROM   DB2ADMIN.WRKFINASSETDEPSUMMARY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
