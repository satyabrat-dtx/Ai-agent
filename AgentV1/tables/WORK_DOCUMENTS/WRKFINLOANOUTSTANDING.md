# DB2ADMIN.WRKFINLOANOUTSTANDING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 229784

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `LOANNO` | CHAR(10) |  |  |  |  |
| 5 | `BUSINESSUNITCODE` | CHAR(3) |  |  |  |  |
| 6 | `LONGDESCRIPTIONBNK` | VARCHAR(200) |  |  |  |  |
| 7 | `LONGDESCRIPTIONBU` | VARCHAR(200) |  |  |  |  |
| 8 | `OPENING` | DECIMAL(18,5) |  |  |  |  |
| 9 | `RECEIPTS` | DECIMAL(18,5) |  |  |  |  |
| 10 | `PAYMENTS` | DECIMAL(18,5) |  |  |  |  |
| 11 | `BALANCE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `BANKWISE` | CHAR(6) |  |  |  |  |
| 13 | `SELECTIONTYPE` | CHAR(2) |  |  |  |  |
| 14 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 15 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINLOANOUTSTANDINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.LOANNO,
       t.BUSINESSUNITCODE,
       t.LONGDESCRIPTIONBNK,
       t.LONGDESCRIPTIONBU,
       t.OPENING,
       t.RECEIPTS,
       t.PAYMENTS,
       t.BALANCE
FROM   DB2ADMIN.WRKFINLOANOUTSTANDING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
