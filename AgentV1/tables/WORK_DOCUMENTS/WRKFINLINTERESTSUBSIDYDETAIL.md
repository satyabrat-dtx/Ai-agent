# DB2ADMIN.WRKFINLINTERESTSUBSIDYDETAIL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 230021

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `BUSINESSUNITCODE` | CHAR(3) |  |  |  |  |
| 4 | `LOANAVAILED` | DECIMAL(18,5) |  |  |  |  |
| 5 | `REPAID` | DECIMAL(18,5) |  |  |  |  |
| 6 | `BALANCEOUTSTANDING` | DECIMAL(18,5) |  |  |  |  |
| 7 | `BANKLOANGL` | CHAR(20) |  |  |  |  |
| 8 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 9 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 10 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 11 | `LOANFINANCIALYEAR` | DECIMAL(4,0) |  |  |  |  |
| 12 | `REPAYMENTDATE` | DECIMAL(4,0) |  |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINLINTERESTSUBSIDYDLTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.BUSINESSUNITCODE,
       t.LOANAVAILED,
       t.REPAID,
       t.BALANCEOUTSTANDING,
       t.BANKLOANGL,
       t.SHORTDESCRIPTION,
       t.FROMDATE,
       t.TODATE,
       t.LOANFINANCIALYEAR
FROM   DB2ADMIN.WRKFINLINTERESTSUBSIDYDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
