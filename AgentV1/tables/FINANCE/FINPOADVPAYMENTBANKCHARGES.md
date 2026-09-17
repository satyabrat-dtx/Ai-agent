# DB2ADMIN.FINPOADVPAYMENTBANKCHARGES

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `FINPOADVANCEPROPOSALCMYCODE`, `FINPOADVANCEPROPOSALCODE`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 227985

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINPOADVANCEPROPOSALCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINPOADVANCEPROPOSALCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 4 | `COMCURRENCYBC` | SMALLINT | NOT NULL |  |  |  |
| 5 | `DOCCURRENCYBC` | SMALLINT | NOT NULL |  |  |  |
| 6 | `GLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `GLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 8 | `AMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `FINPOADVPAYMENTBANKCHARGES.CURRENCYCODE = CURRENCY.CODE` |
| `FINPOADVANCEPROPOSAL_BANKCHARGES` | `FINPOADVANCEPROPOSALCMYCODE`, `FINPOADVANCEPROPOSALCODE` | [`FINPOADVANCEPROPOSAL`](../FINANCE/FINPOADVANCEPROPOSAL.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINPOADVPAYMENTBANKCHARGES.FINPOADVANCEPROPOSALCMYCODE = FINPOADVANCEPROPOSAL.COMPANYCODE AND FINPOADVPAYMENTBANKCHARGES.FINPOADVANCEPROPOSALCODE = FINPOADVANCEPROPOSAL.CODE` |
| `GLMASTER_GL` | `GLCOMPANYCODE`, `GLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINPOADVPAYMENTBANKCHARGES.GLCOMPANYCODE = GLMASTER.COMPANYCODE AND FINPOADVPAYMENTBANKCHARGES.GLCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINPOADVPAYMENTBANKCHARGESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINPOADVANCEPROPOSALCMYCODE,
       t.FINPOADVANCEPROPOSALCODE,
       t.LINE,
       t.CURRENCYCODE,
       t.COMCURRENCYBC,
       t.DOCCURRENCYBC,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.AMOUNT,
       t.REMARK,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.FINPOADVPAYMENTBANKCHARGES t
FETCH FIRST 100 ROWS ONLY;
```
