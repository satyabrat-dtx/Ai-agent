# DB2ADMIN.EINVOICEPAYMENT

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `PAYMENTID`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237229

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PAYMENTID` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `PAYMENTCONDITIONS` | CHAR(4) | NOT NULL |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EINVOICEBODY_PAYMENT` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID` | [`EINVOICEBODY`](../EINVOICING/EINVOICEBODY.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `BODYID` | RESTRICT | `EINVOICEPAYMENT.EINVOICEHEADERCOMPANYCODE = EINVOICEBODY.EINVOICEHEADERCOMPANYCODE AND EINVOICEPAYMENT.EINVOICEHEADERUNIQUEID = EINVOICEBODY.EINVOICEHEADERUNIQUEID AND EINVOICEPAYMENT.EINVOICEBODYID = EINVOICEBODY.BODYID` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `EINVOICEPAYMENT_DETAIL` | [`EINVOICEPAYMENTDETAIL`](../EINVOICING/EINVOICEPAYMENTDETAIL.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEPAYMENTID` | `EINVOICEPAYMENTDETAIL.EINVOICEHEADERCOMPANYCODE = EINVOICEPAYMENT.EINVOICEHEADERCOMPANYCODE AND EINVOICEPAYMENTDETAIL.EINVOICEHEADERUNIQUEID = EINVOICEPAYMENT.EINVOICEHEADERUNIQUEID AND EINVOICEPAYMENTDETAIL.EINVOICEBODYID = EINVOICEPAYMENT.EINVOICEBODYID AND EINVOICEPAYMENTDETAIL.EINVOICEPAYMENTID = EINVOICEPAYMENT.PAYMENTID` |

## Indexes

- `EINVOICEPAYMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.PAYMENTID,
       t.PAYMENTCONDITIONS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.EINVOICEPAYMENT t
FETCH FIRST 100 ROWS ONLY;
```
