# DB2ADMIN.WRKFINBALCONFIRMINVBREAKUP

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 230170

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 6 | `ORDERPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `ORDERPARTNERCODE` | CHAR(8) |  |  |  |  |
| 8 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 9 | `INVOICEDATE` | DATE |  |  |  |  |
| 10 | `POSTINGDATE` | DATE |  |  |  |  |
| 11 | `DUEDATE` | DATE |  |  |  |  |
| 12 | `AMOUNTINDC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 13 | `CLEAREDAMOUNTDC` | DECIMAL(18,5) |  |  |  |  |
| 14 | `OUTSTANDINGAMTDC` | DECIMAL(18,5) |  |  |  |  |
| 15 | `CHEQUENUMBER` | CHAR(20) |  |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINBALCONFIRMINVBREAKUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.BUSINESSUNITCODE,
       t.LINENO,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.ORDERPARTNERTYPE,
       t.ORDERPARTNERCODE,
       t.INVOICENO,
       t.INVOICEDATE,
       t.POSTINGDATE,
       t.DUEDATE
FROM   DB2ADMIN.WRKFINBALCONFIRMINVBREAKUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
