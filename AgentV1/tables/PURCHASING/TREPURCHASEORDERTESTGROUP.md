# DB2ADMIN.TREPURCHASEORDERTESTGROUP

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 2 of 2 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 69553

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(4) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `SEQUENCEGROUP` | DECIMAL(5,0) |  |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TREPURCHASEORDERTESTGROUP.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TREPURCHASEORDERTESTGROUP_GROUP` | [`TREPURCHASEORDERTESTDATA`](../PURCHASING/TREPURCHASEORDERTESTDATA.md) | `PURCHASEORDERCOMPANYCODE`, `GROUPCODE` | `TREPURCHASEORDERTESTDATA.PURCHASEORDERCOMPANYCODE = TREPURCHASEORDERTESTGROUP.COMPANYCODE AND TREPURCHASEORDERTESTDATA.GROUPCODE = TREPURCHASEORDERTESTGROUP.CODE` |
| `TREPURCHASEORDERTESTGROUP_TESTDETAIL` | [`TREPURCHASEORDERTESTDETAIL`](../PURCHASING/TREPURCHASEORDERTESTDETAIL.md) | `TREPURORDTESTGROUPCOMPANYCODE`, `TREPURCHASEORDERTESTGROUPCODE` | `TREPURCHASEORDERTESTDETAIL.TREPURORDTESTGROUPCOMPANYCODE = TREPURCHASEORDERTESTGROUP.COMPANYCODE AND TREPURCHASEORDERTESTDETAIL.TREPURCHASEORDERTESTGROUPCODE = TREPURCHASEORDERTESTGROUP.CODE` |
| `TREPURCHASEORDERTESTGROUP_GROUP` | [`TREWRKPURCHASEORDERTESTDATA`](../PURCHASING/TREWRKPURCHASEORDERTESTDATA.md) | `PURCHASEORDERCOMPANYCODE`, `GROUPCODE` | `TREWRKPURCHASEORDERTESTDATA.PURCHASEORDERCOMPANYCODE = TREPURCHASEORDERTESTGROUP.COMPANYCODE AND TREWRKPURCHASEORDERTESTDATA.GROUPCODE = TREPURCHASEORDERTESTGROUP.CODE` |

## Indexes

- `TREPURCHASEORDERTESTGROUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.SEQUENCEGROUP,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TREPURCHASEORDERTESTGROUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
