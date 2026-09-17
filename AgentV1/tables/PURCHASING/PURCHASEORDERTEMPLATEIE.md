# DB2ADMIN.PURCHASEORDERTEMPLATEIE

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 129796

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MRNPREFIXDIVISIONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 1 | `MRNPREFIXCODE` | CHAR(3) |  | FK | foreign_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `TAXTEMPLATEHEADERTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 5 | `TAXTEMPLATEHEADERCODE` | CHAR(3) |  |  |  |  |
| 6 | `DEFAULTTAXFROM` | INTEGER | NOT NULL |  |  |  |
| 7 | `MULTIPLEMRNFLAG` | INTEGER | NOT NULL |  |  |  |
| 8 | `MRNMODIFYFLAG` | INTEGER | NOT NULL |  |  |  |
| 9 | `TAXTEMPLATEAPPLICABLE` | INTEGER | NOT NULL |  |  |  |
| 10 | `MRNBASEDPLANTREQ` | CHAR(2) |  |  |  |  |
| 11 | `MRNBASEDONSTOCKCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `MRNBASEDONSTOCKCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `USEDFORJOBWORK` | SMALLINT | NOT NULL |  |  |  |
| 14 | `PURCHASETYPE` | CHAR(20) | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `MRNPREFIX_MRNPREFIX` | `COMPANYCODE`, `MRNPREFIXDIVISIONCODE`, `MRNPREFIXCODE` | [`MRNPREFIX`](../OTHER/MRNPREFIX.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `PURCHASEORDERTEMPLATEIE.COMPANYCODE = MRNPREFIX.COMPANYCODE AND PURCHASEORDERTEMPLATEIE.MRNPREFIXDIVISIONCODE = MRNPREFIX.DIVISIONCODE AND PURCHASEORDERTEMPLATEIE.MRNPREFIXCODE = MRNPREFIX.CODE` |
| `STOCKTRANSACTIONTEMPLATE_MRNBASEDONSTOCK` | `MRNBASEDONSTOCKCOMPANYCODE`, `MRNBASEDONSTOCKCODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEORDERTEMPLATEIE.MRNBASEDONSTOCKCOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND PURCHASEORDERTEMPLATEIE.MRNBASEDONSTOCKCODE = STOCKTRANSACTIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERTEMPLATEIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MRNPREFIXDIVISIONCODE,
       t.MRNPREFIXCODE,
       t.COMPANYCODE,
       t.CODE,
       t.TAXTEMPLATEHEADERTEMPLATETYPE,
       t.TAXTEMPLATEHEADERCODE,
       t.DEFAULTTAXFROM,
       t.MULTIPLEMRNFLAG,
       t.MRNMODIFYFLAG,
       t.TAXTEMPLATEAPPLICABLE,
       t.MRNBASEDPLANTREQ,
       t.MRNBASEDONSTOCKCOMPANYCODE
FROM   DB2ADMIN.PURCHASEORDERTEMPLATEIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
