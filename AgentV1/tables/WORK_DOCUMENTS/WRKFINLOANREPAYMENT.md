# DB2ADMIN.WRKFINLOANREPAYMENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 223264

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `BUSINESSUNITCODE` | CHAR(3) |  |  |  |  |
| 4 | `LOANNO` | CHAR(10) |  |  |  |  |
| 5 | `LOANAVAILED` | DECIMAL(18,5) |  |  |  |  |
| 6 | `REPAID` | DECIMAL(18,5) |  |  |  |  |
| 7 | `BALANCEOUTSTANDING` | DECIMAL(18,5) |  |  |  |  |
| 8 | `BANKLOANGL` | CHAR(20) |  |  |  |  |
| 9 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 10 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 11 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 12 | `LOANFINANCIALYEAR` | DECIMAL(4,0) |  |  |  |  |
| 13 | `SELECTIONTYPE` | CHAR(2) |  |  |  |  |
| 14 | `REPAYMENTDATE` | DATE |  |  |  |  |
| 15 | `BANKWISE` | CHAR(6) |  |  |  |  |
| 16 | `BUSINESSUNITWISE` | CHAR(3) |  |  |  |  |
| 17 | `LONGDESCRIPTIONBU` | VARCHAR(200) |  |  |  |  |
| 18 | `LONGDESCRIPTIONBNK` | VARCHAR(200) |  |  |  |  |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINLOANREPAYMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.BUSINESSUNITCODE,
       t.LOANNO,
       t.LOANAVAILED,
       t.REPAID,
       t.BALANCEOUTSTANDING,
       t.BANKLOANGL,
       t.SHORTDESCRIPTION,
       t.FROMDATE,
       t.TODATE
FROM   DB2ADMIN.WRKFINLOANREPAYMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
