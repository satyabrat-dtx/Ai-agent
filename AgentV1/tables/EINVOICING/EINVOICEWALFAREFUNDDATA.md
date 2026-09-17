# DB2ADMIN.EINVOICEWALFAREFUNDDATA

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID`, `WALFAREFUNDDATAID`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 237425

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EINVOICEHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EINVOICEHEADERUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EINVOICEBODYID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `WALFAREFUNDDATAID` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `TYPECODE` | CHAR(4) |  | FK | foreign_key |  |
| 5 | `FUNDRATE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 6 | `AMOUNT` | DECIMAL(14,2) | NOT NULL |  |  |  |
| 7 | `TAXABLEAMOUNT` | DECIMAL(14,2) |  |  |  |  |
| 8 | `TAXRATE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 9 | `WITHHOLDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 10 | `TAXNATURECODE` | CHAR(4) |  | FK | foreign_key |  |
| 11 | `ADMINISTRATIONREFERENCE` | CHAR(36) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EINVOICEBODY_WALFAREFUNDDATA` | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `EINVOICEBODYID` | [`EINVOICEBODY`](../EINVOICING/EINVOICEBODY.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID`, `BODYID` | RESTRICT | `EINVOICEWALFAREFUNDDATA.EINVOICEHEADERCOMPANYCODE = EINVOICEBODY.EINVOICEHEADERCOMPANYCODE AND EINVOICEWALFAREFUNDDATA.EINVOICEHEADERUNIQUEID = EINVOICEBODY.EINVOICEHEADERUNIQUEID AND EINVOICEWALFAREFUNDDATA.EINVOICEBODYID = EINVOICEBODY.BODYID` |
| `FUNDTYPE_TYPE` | `TYPECODE` | [`FUNDTYPE`](../EINVOICING/FUNDTYPE.md) | `CODE` | RESTRICT | `EINVOICEWALFAREFUNDDATA.TYPECODE = FUNDTYPE.CODE` |
| `TAXNATURE_TAXNATURE` | `TAXNATURECODE` | [`TAXNATURE`](../EINVOICING/TAXNATURE.md) | `CODE` | RESTRICT | `EINVOICEWALFAREFUNDDATA.TAXNATURECODE = TAXNATURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EINVOICEWALFAREFUNDDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EINVOICEHEADERCOMPANYCODE,
       t.EINVOICEHEADERUNIQUEID,
       t.EINVOICEBODYID,
       t.WALFAREFUNDDATAID,
       t.TYPECODE,
       t.FUNDRATE,
       t.AMOUNT,
       t.TAXABLEAMOUNT,
       t.TAXRATE,
       t.WITHHOLDINGTAX,
       t.TAXNATURECODE,
       t.ADMINISTRATIONREFERENCE
FROM   DB2ADMIN.EINVOICEWALFAREFUNDDATA t
FETCH FIRST 100 ROWS ONLY;
```
