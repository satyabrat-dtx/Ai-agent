# DB2ADMIN.EINVOICEWITHHOLDINGTAX

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `WITHHOLDINGTAXID`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237476

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `WITHHOLDINGTAXID` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `TYPECODE` | CHAR(4) |  | FK | foreign_key |  |
| 5 | `AMOUNT` | DECIMAL(14,2) | NOT NULL |  |  |  |
| 6 | `RATE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 7 | `PAYMENTREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EINVOICEBODY_WITHHOLDINGTAX` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID` | [`EINVOICEBODY`](../EINVOICING/EINVOICEBODY.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `BODYID` | RESTRICT | `EINVOICEWITHHOLDINGTAX.EINVOICEHEADERCOMPANYCODE = EINVOICEBODY.EINVOICEHEADERCOMPANYCODE AND EINVOICEWITHHOLDINGTAX.EINVOICEHEADERUNIQUEID = EINVOICEBODY.EINVOICEHEADERUNIQUEID AND EINVOICEWITHHOLDINGTAX.EINVOICEBODYID = EINVOICEBODY.BODYID` |
| `WITHHOLDINGTAXPAYMENTREASON_PAYMENTREASON` | `PAYMENTREASONCODE` | [`WITHHOLDINGTAXPAYMENTREASON`](../EINVOICING/WITHHOLDINGTAXPAYMENTREASON.md) | `CODE` | RESTRICT | `EINVOICEWITHHOLDINGTAX.PAYMENTREASONCODE = WITHHOLDINGTAXPAYMENTREASON.CODE` |
| `WITHHOLDINGTAXTYPE_TYPE` | `TYPECODE` | [`WITHHOLDINGTAXTYPE`](../EINVOICING/WITHHOLDINGTAXTYPE.md) | `CODE` | RESTRICT | `EINVOICEWITHHOLDINGTAX.TYPECODE = WITHHOLDINGTAXTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICEWITHHOLDINGTAXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.WITHHOLDINGTAXID,
       t.TYPECODE,
       t.AMOUNT,
       t.RATE,
       t.PAYMENTREASONCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.EINVOICEWITHHOLDINGTAX t
FETCH FIRST 100 ROWS ONLY;
```
