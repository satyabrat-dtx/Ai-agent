# DB2ADMIN.EINVOICEPAYMENTDETAIL

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEPAYMENTID`, `DETAILID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237273

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EINVOICEPAYMENTID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `DETAILID` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `BENEFICIARY` | VARCHAR(400) |  |  |  |  |
| 6 | `EIPAYMENTTYPECODE` | CHAR(4) |  | FK | foreign_key |  |
| 7 | `PAYMENTREFERENCEDATE` | DATE |  |  |  |  |
| 8 | `PAYMENTDAYS` | INTEGER | NOT NULL |  |  |  |
| 9 | `PAYMENTDUEDATE` | DATE |  |  |  |  |
| 10 | `VALUE` | DECIMAL(14,2) | NOT NULL |  |  |  |
| 11 | `BANK` | VARCHAR(160) |  |  |  |  |
| 12 | `IBAN` | CHAR(34) |  |  |  |  |
| 13 | `ABI` | CHAR(5) |  |  |  |  |
| 14 | `CAB` | CHAR(5) |  |  |  |  |
| 15 | `BIC` | CHAR(11) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EINVOICEPAYMENT_DETAIL` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `EINVOICEPAYMENTID` | [`EINVOICEPAYMENT`](../EINVOICING/EINVOICEPAYMENT.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `PAYMENTID` | RESTRICT | `EINVOICEPAYMENTDETAIL.EINVOICEHEADERCOMPANYCODE = EINVOICEPAYMENT.EINVOICEHEADERCOMPANYCODE AND EINVOICEPAYMENTDETAIL.EINVOICEHEADERUNIQUEID = EINVOICEPAYMENT.EINVOICEHEADERUNIQUEID AND EINVOICEPAYMENTDETAIL.EINVOICEBODYID = EINVOICEPAYMENT.EINVOICEBODYID AND EINVOICEPAYMENTDETAIL.EINVOICEPAYMENTID = EINVOICEPAYMENT.PAYMENTID` |
| `EIPAYMENTTYPE_EIPAYMENTTYPE` | `EIPAYMENTTYPECODE` | [`EIPAYMENTTYPE`](../EINVOICING/EIPAYMENTTYPE.md) | `CODE` | RESTRICT | `EINVOICEPAYMENTDETAIL.EIPAYMENTTYPECODE = EIPAYMENTTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICEPAYMENTDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.EINVOICEPAYMENTID,
       t.DETAILID,
       t.BENEFICIARY,
       t.EIPAYMENTTYPECODE,
       t.PAYMENTREFERENCEDATE,
       t.PAYMENTDAYS,
       t.PAYMENTDUEDATE,
       t.VALUE,
       t.BANK
FROM   DB2ADMIN.EINVOICEPAYMENTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
