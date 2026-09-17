# DB2ADMIN.WRKLOANINTERESTSUBSIDY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LOANNO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 228896

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LTEUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 2 | `LTYPEUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `LOANTYPECODE` | CHAR(10) |  |  |  |  |
| 4 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 5 | `BUSINESSUNIT` | CHAR(5) |  |  |  |  |
| 6 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 7 | `BANKGLCODE` | CHAR(20) |  |  |  |  |
| 8 | `TOTALINTEREST` | DECIMAL(18,5) |  |  |  |  |
| 9 | `TOTALSUBSIDY` | DECIMAL(18,5) |  |  |  |  |
| 10 | `INTERESTPAID` | DECIMAL(18,5) |  |  |  |  |
| 11 | `INTERESTPAYABLE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `SUBSIDYRECEIVABLE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `SUBSIDYRECEIVED` | DECIMAL(18,5) |  |  |  |  |
| 14 | `LOANNO` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 16 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 17 | `LASTINTERESTDATE` | DATE |  |  |  |  |
| 18 | `LASTSUBSIDYDATE` | DATE |  |  |  |  |
| 19 | `GLDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 20 | `LONGDESCRIPTIONBU` | VARCHAR(80) |  |  |  |  |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKLOANINTERESTSUBSIDYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LTEUGENGROUPTYPECOMPANYCODE,
       t.LTYPEUSERGENERICGROUPTYPECODE,
       t.LOANTYPECODE,
       t.CREATIONTIMESTAMP,
       t.BUSINESSUNIT,
       t.LINENO,
       t.BANKGLCODE,
       t.TOTALINTEREST,
       t.TOTALSUBSIDY,
       t.INTERESTPAID,
       t.INTERESTPAYABLE
FROM   DB2ADMIN.WRKLOANINTERESTSUBSIDY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
