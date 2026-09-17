# DB2ADMIN.WRKFINASSETDEPRECIATION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178270

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
| 10 | `ASSTCODE` | CHAR(10) |  |  |  |  |
| 11 | `ASSETDESC` | VARCHAR(200) |  |  |  |  |
| 12 | `DATEOFCAPITALIZATION` | DATE |  |  |  |  |
| 13 | `CAPITALIZEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `AMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 15 | `NETBOOKVALUE` | DECIMAL(18,5) |  |  |  |  |
| 16 | `POSTINGDATE` | DATE |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

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
FROM   DB2ADMIN.WRKFINASSETDEPRECIATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
