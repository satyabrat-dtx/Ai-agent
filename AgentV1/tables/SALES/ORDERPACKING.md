# DB2ADMIN.ORDERPACKING

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 36
- **Primary key**: `COMPANYCODE`, `ORDPACKINGSALORDERCOUNTERCODE`, `ORDPACKINGSALESORDERCODE`, `ORDPACKINGORDERLINE`, `ORDPACKINGORDERSUBLINE`, `ORDPACKINGCOMPONENTORDERLINE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 127258

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDPACKINGSALORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ORDPACKINGSALESORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ORDPACKINGORDERLINE` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ORDPACKINGORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `ORDPACKINGCOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 19 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 20 | `PACKINGGROUP` | CHAR(3) |  |  |  |  |
| 21 | `PACKINGTYPE` | CHAR(1) |  |  |  |  |
| 22 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `WEIGHTQTY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `FLAG` | CHAR(1) |  |  |  |  |
| 25 | `NETWEIGHTQTY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `YOURREFERENCE` | VARCHAR(200) |  |  |  |  |
| 27 | `LEFTOVERQTY` | DECIMAL(18,5) |  |  |  |  |
| 28 | `USERQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 30 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 31 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 32 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 33 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 34 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ORDERPACKING.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ORDERPACKING.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ORDERPACKING.ITEMTYPECODE = ITEMTYPE.CODE` |
| `SALESORDERLINE_ORDPACKING` | `COMPANYCODE`, `ORDPACKINGSALORDERCOUNTERCODE`, `ORDPACKINGSALESORDERCODE`, `ORDPACKINGORDERLINE`, `ORDPACKINGORDERSUBLINE`, `ORDPACKINGCOMPONENTORDERLINE` | [`SALESORDERLINE`](../SALES/SALESORDERLINE.md) | `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE` | RESTRICT | `ORDERPACKING.COMPANYCODE = SALESORDERLINE.SALESORDERCOMPANYCODE AND ORDERPACKING.ORDPACKINGSALORDERCOUNTERCODE = SALESORDERLINE.SALESORDERCOUNTERCODE AND ORDERPACKING.ORDPACKINGSALESORDERCODE = SALESORDERLINE.SALESORDERCODE AND ORDERPACKING.ORDPACKINGORDERLINE = SALESORDERLINE.ORDERLINE AND ORDERPACKING.ORDPACKINGORDERSUBLINE = SALESORDERLINE.ORDERSUBLINE AND ORDERPACKING.ORDPACKINGCOMPONENTORDERLINE = SALESORDERLINE.COMPONENTORDERLINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ORDERPACKINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDPACKINGSALORDERCOUNTERCODE,
       t.ORDPACKINGSALESORDERCODE,
       t.ORDPACKINGORDERLINE,
       t.ORDPACKINGORDERSUBLINE,
       t.ORDPACKINGCOMPONENTORDERLINE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.ORDERPACKING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
