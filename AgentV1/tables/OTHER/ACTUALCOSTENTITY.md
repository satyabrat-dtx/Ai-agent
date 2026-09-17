# DB2ADMIN.ACTUALCOSTENTITY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 38
- **Primary key**: `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 50871

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 3 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 4 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 5 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 6 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 7 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 8 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 9 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 10 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 11 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 12 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 13 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) |  |  |  |  |
| 14 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 15 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 16 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 17 | `CUSTOMERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 19 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 20 | `SUPPLIERCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 21 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 23 | `PROJECTCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 25 | `STATISTICALGROUPCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 26 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 27 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 28 | `EARLIESTTRANSACTIONDATE` | DATE |  |  |  |  |
| 29 | `DATETOSTARTCALCULATINGFROM` | DATE |  |  |  |  |
| 30 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 31 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 32 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 33 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 34 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 36 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 37 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ACTUALCOSTENTITY.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACTUALCOSTENTITY.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ACTUALCOSTENTITY.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACTUALCOSTENTITY_ACTUALCOSTENTITYCLOSINGBALANCE` | [`ACTUALCOSTENTITYCLOSINGBLN`](../OTHER/ACTUALCOSTENTITYCLOSINGBLN.md) | `ACTUALCOSTENTITYCOMPANYCODE`, `ACTUALCOSTENTITYNUMBERID` | `ACTUALCOSTENTITYCLOSINGBLN.ACTUALCOSTENTITYCOMPANYCODE = ACTUALCOSTENTITY.COMPANYCODE AND ACTUALCOSTENTITYCLOSINGBLN.ACTUALCOSTENTITYNUMBERID = ACTUALCOSTENTITY.NUMBERID` |

## Indexes

- UNIQUE `ACTUALCOSTENTITY1` (COMPANYCODE, WAREHOUSEACCOUNTINGGROUPCODE, ITEMTYPECODE, DECOSUBCODE01, DECOSUBCODE02, DECOSUBCODE03, DECOSUBCODE04, DECOSUBCODE05, DECOSUBCODE06, DECOSUBCODE07, DECOSUBCODE08, DECOSUBCODE09, DECOSUBCODE10, LOTCODE, ELEMENTSSUBCODEKEY, ELEMENTSCODE, QUALITYLEVELCODE, PROJECTCODE, STATISTICALGROUPCODE, CUSTOMERCODE, SUPPLIERCODE)
- `ACTUALCOSTENTITYUID` (ABSUNIQUEID)
- `ACTUALCOSTENTITY3` (COMPANYCODE, WAREHOUSEACCOUNTINGGROUPCODE, ITEMTYPECODE, DECOSUBCODE01, DATETOSTARTCALCULATINGFROM, DECOSUBCODE02, DECOSUBCODE03, DECOSUBCODE04, DECOSUBCODE05, DECOSUBCODE06, DECOSUBCODE07, DECOSUBCODE08, DECOSUBCODE09, DECOSUBCODE10)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.ITEMTYPECODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05,
       t.DECOSUBCODE06,
       t.DECOSUBCODE07,
       t.DECOSUBCODE08,
       t.DECOSUBCODE09
FROM   DB2ADMIN.ACTUALCOSTENTITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
