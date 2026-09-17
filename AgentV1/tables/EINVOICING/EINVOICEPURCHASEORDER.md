# DB2ADMIN.EINVOICEPURCHASEORDER

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `PURCHASEORDERID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237329

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PURCHASEORDERID` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `EINVOICELINES` | CLOB(1000000) |  |  |  |  |
| 5 | `DOCUMENTNUMBER` | CHAR(20) | NOT NULL |  |  |  |
| 6 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 7 | `DOCUMENTLINE` | CHAR(20) |  |  |  |  |
| 8 | `PROJECTCODE` | VARCHAR(100) |  |  |  |  |
| 9 | `CUPCODE` | CHAR(15) |  |  |  |  |
| 10 | `CIGCODE` | CHAR(15) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EINVOICEBODY_PURCHASEORDER` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID` | [`EINVOICEBODY`](../EINVOICING/EINVOICEBODY.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `BODYID` | RESTRICT | `EINVOICEPURCHASEORDER.EINVOICEHEADERCOMPANYCODE = EINVOICEBODY.EINVOICEHEADERCOMPANYCODE AND EINVOICEPURCHASEORDER.EINVOICEHEADERUNIQUEID = EINVOICEBODY.EINVOICEHEADERUNIQUEID AND EINVOICEPURCHASEORDER.EINVOICEBODYID = EINVOICEBODY.BODYID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICEPURCHASEORDERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.PURCHASEORDERID,
       t.EINVOICELINES,
       t.DOCUMENTNUMBER,
       t.DOCUMENTDATE,
       t.DOCUMENTLINE,
       t.PROJECTCODE,
       t.CUPCODE,
       t.CIGCODE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.EINVOICEPURCHASEORDER t
FETCH FIRST 100 ROWS ONLY;
```
