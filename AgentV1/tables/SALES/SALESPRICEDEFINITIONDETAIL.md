# DB2ADMIN.SALESPRICEDEFINITIONDETAIL

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `SALPRICEDEFINITIONCOMPANYCODE`, `SALESPRICEDEFINITIONNUMBERID`, `NUMBERLINEID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 25775

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALPRICEDEFINITIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALESPRICEDEFINITIONNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `QUALITYLEVELITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 4 | `BREAKDOWNLIMIT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 5 | `SOURCEPRICETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `NUMBERLINEID` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `COMPOUNDPRICETYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `PRICETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `PRICEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 11 | `PRICESIGN` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPOUNDPRICETYPE_COMPOUNDPRICETYPE` | `SALPRICEDEFINITIONCOMPANYCODE`, `COMPOUNDPRICETYPECODE` | [`COMPOUNDPRICETYPE`](../SALES/COMPOUNDPRICETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESPRICEDEFINITIONDETAIL.SALPRICEDEFINITIONCOMPANYCODE = COMPOUNDPRICETYPE.COMPANYCODE AND SALESPRICEDEFINITIONDETAIL.COMPOUNDPRICETYPECODE = COMPOUNDPRICETYPE.CODE` |
| `SALESPRICEDEFINITION_PRICEDETAIL` | `SALPRICEDEFINITIONCOMPANYCODE`, `SALESPRICEDEFINITIONNUMBERID` | [`SALESPRICEDEFINITION`](../SALES/SALESPRICEDEFINITION.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `SALESPRICEDEFINITIONDETAIL.SALPRICEDEFINITIONCOMPANYCODE = SALESPRICEDEFINITION.COMPANYCODE AND SALESPRICEDEFINITIONDETAIL.SALESPRICEDEFINITIONNUMBERID = SALESPRICEDEFINITION.NUMBERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESPRICEDEFINITIONDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALPRICEDEFINITIONCOMPANYCODE,
       t.SALESPRICEDEFINITIONNUMBERID,
       t.QUALITYLEVELITEMTYPECODE,
       t.QUALITYLEVELCODE,
       t.BREAKDOWNLIMIT,
       t.SOURCEPRICETYPE,
       t.NUMBERLINEID,
       t.COMPOUNDPRICETYPECODE,
       t.PRICETYPE,
       t.PRICE,
       t.PRICEPERCENTAGE,
       t.PRICESIGN
FROM   DB2ADMIN.SALESPRICEDEFINITIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
