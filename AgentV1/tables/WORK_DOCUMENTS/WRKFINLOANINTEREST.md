# DB2ADMIN.WRKFINLOANINTEREST

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `INTERESTDATETIME`, `COMPANYCODE`, `LNOLTEUGENERICGROUPTYPECODE`, `LOANNOLOANTYPECODE`, `LOANNOLOANNO`, `FROMDATE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 227111

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `INTERESTDATETIME` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LNOLTEUGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `LOANNOLOANTYPECODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `LOANNOLOANNO` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 5 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 6 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 8 | `NOOFDAYS` | INTEGER | NOT NULL |  |  |  |
| 9 | `OUTSTANDINGAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `INTERESTRATE` | DECIMAL(6,2) |  |  |  |  |
| 11 | `INTERESTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINLOANINTERESTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.INTERESTDATETIME,
       t.COMPANYCODE,
       t.LNOLTEUGENERICGROUPTYPECODE,
       t.LOANNOLOANTYPECODE,
       t.LOANNOLOANNO,
       t.FROMDATE,
       t.LINENO,
       t.TODATE,
       t.NOOFDAYS,
       t.OUTSTANDINGAMOUNT,
       t.INTERESTRATE,
       t.INTERESTAMOUNT
FROM   DB2ADMIN.WRKFINLOANINTEREST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
