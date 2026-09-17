# DB2ADMIN.FINIMPFCPAYMENTFORLOAN

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `FINIMPORTFCPAYMENTCOMPANYCODE`, `FINIMPORTFCPAYMENTCODE`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 226713

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINIMPORTFCPAYMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINIMPORTFCPAYMENTCODE` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENUMBER` | DECIMAL(18,5) | NOT NULL | PK | primary_key |  |
| 3 | `LOANMASTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `LMLTEUSERGENERICGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `LOANMASTERLOANTYPECODE` | CHAR(10) |  | FK | foreign_key |  |
| 6 | `LOANMASTERLOANNO` | CHAR(10) |  | FK | foreign_key |  |
| 7 | `LOANAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINIMPORTFCPAYMENT_LOAN` | `FINIMPORTFCPAYMENTCOMPANYCODE`, `FINIMPORTFCPAYMENTCODE` | [`FINIMPORTFCPAYMENT`](../FINANCE/FINIMPORTFCPAYMENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINIMPFCPAYMENTFORLOAN.FINIMPORTFCPAYMENTCOMPANYCODE = FINIMPORTFCPAYMENT.COMPANYCODE AND FINIMPFCPAYMENTFORLOAN.FINIMPORTFCPAYMENTCODE = FINIMPORTFCPAYMENT.CODE` |
| `FINLOANMASTER_LOANMASTER` | `LOANMASTERCOMPANYCODE`, `LMLTEUSERGENERICGROUPTYPECODE`, `LOANMASTERLOANTYPECODE`, `LOANMASTERLOANNO` | [`FINLOANMASTER`](../FINANCE/FINLOANMASTER.md) | `COMPANYCODE`, `LTYPEUSERGENERICGROUPTYPECODE`, `LOANTYPECODE`, `LOANNO` | RESTRICT | `FINIMPFCPAYMENTFORLOAN.LOANMASTERCOMPANYCODE = FINLOANMASTER.COMPANYCODE AND FINIMPFCPAYMENTFORLOAN.LMLTEUSERGENERICGROUPTYPECODE = FINLOANMASTER.LTYPEUSERGENERICGROUPTYPECODE AND FINIMPFCPAYMENTFORLOAN.LOANMASTERLOANTYPECODE = FINLOANMASTER.LOANTYPECODE AND FINIMPFCPAYMENTFORLOAN.LOANMASTERLOANNO = FINLOANMASTER.LOANNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINIMPFCPAYMENTFORLOANUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINIMPORTFCPAYMENTCOMPANYCODE,
       t.FINIMPORTFCPAYMENTCODE,
       t.LINENUMBER,
       t.LOANMASTERCOMPANYCODE,
       t.LMLTEUSERGENERICGROUPTYPECODE,
       t.LOANMASTERLOANTYPECODE,
       t.LOANMASTERLOANNO,
       t.LOANAMOUNT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.FINIMPFCPAYMENTFORLOAN t
FETCH FIRST 100 ROWS ONLY;
```
