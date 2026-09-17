# DB2ADMIN.ITEMVSEVENTGLMAP

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'ITEM')
- **Roles**: `business_data`
- **Columns**: 44
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `EVENTCODE`, `MRNPREFIXCODE`, `INVOICETYPECODE`, `ITEMTYPECODE`, `DEMANDTEMPLATECODE`, `WORKCENTERCODE`, `OPERATIONCODE`, `USERGENERICGRPCODE`, `USERGENERICGRPNAMECODE`, `LOGICALWAREHOUSECODE`, `STOCKTRANSACTIONTEMPLATECODE`, `DOCUMENT`, `TEMPLATECODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 10 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 222542

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EVENTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 3 | `MRNPREFIXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 6 | `INVOICETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 8 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 9 | `DEMANDTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 10 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 11 | `OPERATIONCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 12 | `USERGENERICGRPCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 13 | `USERGENERICGRPNAMETYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 14 | `USERGENERICGRPNAMECODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 16 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 17 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 18 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 19 | `BOOKINGFOR` | CHAR(1) |  |  |  |  |
| 20 | `DOCUMENT` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 21 | `TEMPLATECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 22 | `DEBITGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 23 | `DEBITGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 24 | `CREDITGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 25 | `CREDITGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 26 | `DIFFERENCEGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `DIFFERENCEGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 28 | `COSTDIFFERENCEGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 29 | `COSTDIFFERENCEGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 30 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 31 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 32 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 33 | `GROUPBYPROJECT` | SMALLINT | NOT NULL |  |  |  |
| 34 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 35 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 36 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 37 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 38 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 39 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 40 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 41 | `PROCOSTVARIANCECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 42 | `PRODUCTIONCOSTVARIANCECODE` | CHAR(20) |  | FK | foreign_key |  |
| 43 | `COSTINGCALCULATION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 10

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITEMVSEVENTGLMAP.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMVSEVENTGLMAP.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND ITEMVSEVENTGLMAP.COUNTERCODE = COUNTER.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMVSEVENTGLMAP.COMPANYCODE = DIVISION.COMPANYCODE AND ITEMVSEVENTGLMAP.DIVISIONCODE = DIVISION.CODE` |
| `EVENTMASTER_EVENT` | `EVENTCODE` | [`EVENTMASTER`](../CORE_MASTER/EVENTMASTER.md) | `CODE` | RESTRICT | `ITEMVSEVENTGLMAP.EVENTCODE = EVENTMASTER.CODE` |
| `GLMASTER_COSTDIFFERENCEGL` | `COSTDIFFERENCEGLCOMPANYCODE`, `COSTDIFFERENCEGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMVSEVENTGLMAP.COSTDIFFERENCEGLCOMPANYCODE = GLMASTER.COMPANYCODE AND ITEMVSEVENTGLMAP.COSTDIFFERENCEGLCODE = GLMASTER.CODE` |
| `GLMASTER_CREDITGL` | `CREDITGLCOMPANYCODE`, `CREDITGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMVSEVENTGLMAP.CREDITGLCOMPANYCODE = GLMASTER.COMPANYCODE AND ITEMVSEVENTGLMAP.CREDITGLCODE = GLMASTER.CODE` |
| `GLMASTER_DEBITGL` | `DEBITGLCOMPANYCODE`, `DEBITGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMVSEVENTGLMAP.DEBITGLCOMPANYCODE = GLMASTER.COMPANYCODE AND ITEMVSEVENTGLMAP.DEBITGLCODE = GLMASTER.CODE` |
| `GLMASTER_DIFFERENCEGL` | `DIFFERENCEGLCOMPANYCODE`, `DIFFERENCEGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMVSEVENTGLMAP.DIFFERENCEGLCOMPANYCODE = GLMASTER.COMPANYCODE AND ITEMVSEVENTGLMAP.DIFFERENCEGLCODE = GLMASTER.CODE` |
| `GLMASTER_PRODUCTIONCOSTVARIANCE` | `PROCOSTVARIANCECOMPANYCODE`, `PRODUCTIONCOSTVARIANCECODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMVSEVENTGLMAP.PROCOSTVARIANCECOMPANYCODE = GLMASTER.COMPANYCODE AND ITEMVSEVENTGLMAP.PRODUCTIONCOSTVARIANCECODE = GLMASTER.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMVSEVENTGLMAP.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ITEMVSEVENTGLMAP.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITEMVSEVENTGLMAPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EVENTCODE,
       t.DIVISIONCODE,
       t.MRNPREFIXCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.INVOICETYPECODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.DEMANDTEMPLATECODE,
       t.WORKCENTERCODE,
       t.OPERATIONCODE
FROM   DB2ADMIN.ITEMVSEVENTGLMAP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
