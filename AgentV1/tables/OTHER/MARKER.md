# DB2ADMIN.MARKER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `PRODUCTIONORDERCODE`, `MARKERCODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126979

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODUCTIONORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `USERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 4 | `MARKERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `LAYLENGTH` | DECIMAL(9,5) |  |  |  |  |
| 9 | `NUMOFLAYERS` | INTEGER | NOT NULL |  |  |  |
| 10 | `SHRINKAGEGROUP` | CHAR(10) |  |  |  |  |
| 11 | `WIDTHRANGE` | DECIMAL(5,2) |  |  |  |  |
| 12 | `WIDTHRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 13 | `GSMRANGE` | DECIMAL(5,2) |  |  |  |  |
| 14 | `GSMRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `STEP` | CHAR(1) |  |  |  |  |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MARKER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `MARKER_LINE` | [`MARKERDETAIL`](../OTHER/MARKERDETAIL.md) | `MARKERCOMPANYCODE`, `MARKERPRODUCTIONORDERCODE`, `MARKERMARKERCODE` | `MARKERDETAIL.MARKERCOMPANYCODE = MARKER.COMPANYCODE AND MARKERDETAIL.MARKERPRODUCTIONORDERCODE = MARKER.PRODUCTIONORDERCODE AND MARKERDETAIL.MARKERMARKERCODE = MARKER.MARKERCODE` |

## Indexes

- `MARKERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODUCTIONORDERCODE,
       t.USERGENERICGROUPTYPECODE,
       t.COLORCODE,
       t.MARKERCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.LAYLENGTH,
       t.NUMOFLAYERS,
       t.SHRINKAGEGROUP,
       t.WIDTHRANGE
FROM   DB2ADMIN.MARKER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
