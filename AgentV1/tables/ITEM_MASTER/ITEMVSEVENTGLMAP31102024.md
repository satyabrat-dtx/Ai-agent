# DB2ADMIN.ITEMVSEVENTGLMAP31102024

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `no_primary_key`
- **Columns**: 41
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 222487

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EVENTCODE` | CHAR(15) | NOT NULL |  |  |  |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `MRNPREFIXCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `INVOICETYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 7 | `USERGENERICGRPCODE` | CHAR(4) | NOT NULL |  |  |  |
| 8 | `USERGENERICGRPNAMETYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 9 | `USERGENERICGRPNAMECODE` | CHAR(10) | NOT NULL |  |  |  |
| 10 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 11 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL |  |  |  |
| 12 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 13 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 14 | `BOOKINGFOR` | CHAR(1) |  |  |  |  |
| 15 | `DOCUMENT` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `TEMPLATECODE` | CHAR(8) | NOT NULL |  |  |  |
| 17 | `DEBITGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `DEBITGLCODE` | CHAR(20) |  |  |  |  |
| 19 | `CREDITGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `CREDITGLCODE` | CHAR(20) |  |  |  |  |
| 21 | `DIFFERENCEGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `DIFFERENCEGLCODE` | CHAR(20) |  |  |  |  |
| 23 | `EFFECTIVEFROMDATE` | DATE | NOT NULL |  |  |  |
| 24 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 25 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 26 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 27 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 28 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 29 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 33 | `COUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 34 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 35 | `DEMANDTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 36 | `WORKCENTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 37 | `OPERATIONCODE` | CHAR(8) | NOT NULL |  |  |  |
| 38 | `COSTDIFFERENCEGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `COSTDIFFERENCEGLCODE` | CHAR(20) |  |  |  |  |
| 40 | `GROUPBYPROJECT` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EVENTCODE,
       t.DIVISIONCODE,
       t.MRNPREFIXCODE,
       t.INVOICETYPECODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.USERGENERICGRPCODE,
       t.USERGENERICGRPNAMETYPECODE,
       t.USERGENERICGRPNAMECODE,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE
FROM   DB2ADMIN.ITEMVSEVENTGLMAP31102024 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
