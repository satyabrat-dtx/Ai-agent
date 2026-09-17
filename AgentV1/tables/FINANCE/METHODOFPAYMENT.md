# DB2ADMIN.METHODOFPAYMENT

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `CODE`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93844

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `BANK` | SMALLINT | NOT NULL |  |  |  |
| 5 | `DIRECTDEBIT` | SMALLINT | NOT NULL |  |  |  |
| 6 | `DEPOSITSLIP` | SMALLINT | NOT NULL |  |  |  |
| 7 | `VOUCHERREFSPEC` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CLEARINGNUMBER` | SMALLINT | NOT NULL |  |  |  |
| 9 | `BIC` | SMALLINT | NOT NULL |  |  |  |
| 10 | `IBAN` | SMALLINT | NOT NULL |  |  |  |
| 11 | `BANKMASTER` | SMALLINT | NOT NULL |  |  |  |
| 12 | `CHECKSCL` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `METHODOFPAYMENT_METHODPAYMENTTYPE` | [`PAYMENTTYPE`](../FINANCE/PAYMENTTYPE.md) | `METHODPAYMENTTYPECODE` | `PAYMENTTYPE.METHODPAYMENTTYPECODE = METHODOFPAYMENT.CODE` |

## Indexes

- `METHODOFPAYMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.BANK,
       t.DIRECTDEBIT,
       t.DEPOSITSLIP,
       t.VOUCHERREFSPEC,
       t.CLEARINGNUMBER,
       t.BIC,
       t.IBAN,
       t.BANKMASTER
FROM   DB2ADMIN.METHODOFPAYMENT t
FETCH FIRST 100 ROWS ONLY;
```
