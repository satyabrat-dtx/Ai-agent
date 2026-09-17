# DB2ADMIN.QUALITYFORMULA

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `ITEMTYPECODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 85596

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `CODE` | CHAR(6) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QUALITYFORMULA.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUALITYFORMULA.COMPANYCODE = DIVISION.COMPANYCODE AND QUALITYFORMULA.DIVISIONCODE = DIVISION.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `QUALITYFORMULA_FORMULA` | [`QATEST`](../QUALITY/QATEST.md) | `COMPANYCODE`, `DIVISIONCODE`, `ITEMTYPECODE`, `FORMULACODE` | `QATEST.COMPANYCODE = QUALITYFORMULA.COMPANYCODE AND QATEST.DIVISIONCODE = QUALITYFORMULA.DIVISIONCODE AND QATEST.ITEMTYPECODE = QUALITYFORMULA.ITEMTYPECODE AND QATEST.FORMULACODE = QUALITYFORMULA.CODE` |
| `QUALITYFORMULA_LINE` | [`QUALITYFORMULADETAIL`](../QUALITY/QUALITYFORMULADETAIL.md) | `QUALITYFORMULACOMPANYCODE`, `QUALITYFORMULADIVISIONCODE`, `QUALITYFORMULAITEMTYPECODE`, `QUALITYFORMULACODE` | `QUALITYFORMULADETAIL.QUALITYFORMULACOMPANYCODE = QUALITYFORMULA.COMPANYCODE AND QUALITYFORMULADETAIL.QUALITYFORMULADIVISIONCODE = QUALITYFORMULA.DIVISIONCODE AND QUALITYFORMULADETAIL.QUALITYFORMULAITEMTYPECODE = QUALITYFORMULA.ITEMTYPECODE AND QUALITYFORMULADETAIL.QUALITYFORMULACODE = QUALITYFORMULA.CODE` |

## Indexes

- `QUALITYFORMULAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.QUALITYFORMULA t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
