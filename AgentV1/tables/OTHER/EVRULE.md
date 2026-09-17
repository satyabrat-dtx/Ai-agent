# DB2ADMIN.EVRULE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `CATEGORYICSTABLECODE`, `CATEGORYCODE`, `SUBCTGSUBCATEGORYICSTABLECODE`, `SUBCATEGORYSUBCATEGORYCODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 151487

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CATEGORYICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CATEGORYCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SUBCTGSUBCATEGORYICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SUBCATEGORYSUBCATEGORYCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 6 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 7 | `GENDERSPECIFIC` | SMALLINT | NOT NULL |  |  |  |
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
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EVRULE.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_CATEGORY` | `COMPANYCODE`, `CATEGORYICSTABLECODE`, `CATEGORYCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `EVRULE.COMPANYCODE = ICSENTITY.COMPANYCODE AND EVRULE.CATEGORYICSTABLECODE = ICSENTITY.ICSTABLECODE AND EVRULE.CATEGORYCODE = ICSENTITY.CODE` |
| `SUBCATEGORY_SUBCATEGORY` | `COMPANYCODE`, `CATEGORYICSTABLECODE`, `CATEGORYCODE`, `SUBCTGSUBCATEGORYICSTABLECODE`, `SUBCATEGORYSUBCATEGORYCODE` | [`SUBCATEGORY`](../CORE_MASTER/SUBCATEGORY.md) | `COMPANYCODE`, `CATEGORYICSTABLECODE`, `CATEGORYCODE`, `SUBCATEGORYICSTABLECODE`, `SUBCATEGORYCODE` | RESTRICT | `EVRULE.COMPANYCODE = SUBCATEGORY.COMPANYCODE AND EVRULE.CATEGORYICSTABLECODE = SUBCATEGORY.CATEGORYICSTABLECODE AND EVRULE.CATEGORYCODE = SUBCATEGORY.CATEGORYCODE AND EVRULE.SUBCTGSUBCATEGORYICSTABLECODE = SUBCATEGORY.SUBCATEGORYICSTABLECODE AND EVRULE.SUBCATEGORYSUBCATEGORYCODE = SUBCATEGORY.SUBCATEGORYCODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `EVRULE_LINE` | [`EVRULEDETAIL`](../OTHER/EVRULEDETAIL.md) | `EVRULECOMPANYCODE`, `EVRULECATEGORYICSTABLECODE`, `EVRULECATEGORYCODE`, `EVRLSUBCTGSUBCTGICSTABLECODE`, `EVRLSUBCTGSUBCATEGORYCODE`, `EVRULEEFFECTIVEFROMDATE` | `EVRULEDETAIL.EVRULECOMPANYCODE = EVRULE.COMPANYCODE AND EVRULEDETAIL.EVRULECATEGORYICSTABLECODE = EVRULE.CATEGORYICSTABLECODE AND EVRULEDETAIL.EVRULECATEGORYCODE = EVRULE.CATEGORYCODE AND EVRULEDETAIL.EVRLSUBCTGSUBCTGICSTABLECODE = EVRULE.SUBCTGSUBCATEGORYICSTABLECODE AND EVRULEDETAIL.EVRLSUBCTGSUBCATEGORYCODE = EVRULE.SUBCATEGORYSUBCATEGORYCODE AND EVRULEDETAIL.EVRULEEFFECTIVEFROMDATE = EVRULE.EFFECTIVEFROMDATE` |

## Indexes

- `EVRULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.SUBCTGSUBCATEGORYICSTABLECODE,
       t.SUBCATEGORYSUBCATEGORYCODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.GENDERSPECIFIC,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.EVRULE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
