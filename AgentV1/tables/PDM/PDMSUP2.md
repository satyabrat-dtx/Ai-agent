# DB2ADMIN.PDMSUP2

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `PDMSUP0COMPANYCODE`, `PDMSUP0AFRECTYCODE`, `PDMSUP0AFTPREC`, `PDMSUP0AFCITEM`, `PDMSUP0AFVERNR`, `PDMSUP0AFVERST`, `PDMSUP0CSTSUPPCSMSUPPLIERTYPE`, `PDMSUP0CSTSUPPCSMSUPPLIERCODE`, `AF_SIZESIZESTYPECODE`, `AF_SIZECODE`, `AF_LINKEDSIZESIZESTYPECODE`, `AF_LINKEDSIZECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 48165

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PDMSUP0COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PDMSUP0AFRECTYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PDMSUP0AFTPREC` | DECIMAL(1,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PDMSUP0AFCITEM` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PDMSUP0AFVERNR` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PDMSUP0AFVERST` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `PDMSUP0CSTSUPPCSMSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `PDMSUP0CSTSUPPCSMSUPPLIERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `AF_SIZESIZESTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 9 | `AF_SIZECODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `AF_SIZCD` | CHAR(50) |  |  |  |  |
| 11 | `AF_SIZDS` | VARCHAR(255) |  |  |  |  |
| 12 | `AF_SIZESIZESTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `AF_LINKEDSIZESIZESTYPECMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 15 | `AF_LINKEDSIZESIZESTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 16 | `AF_LINKEDSIZECODE` | CHAR(10) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PDMSUP0_SIZES` | `PDMSUP0COMPANYCODE`, `PDMSUP0AFRECTYCODE`, `PDMSUP0AFTPREC`, `PDMSUP0AFCITEM`, `PDMSUP0AFVERNR`, `PDMSUP0AFVERST`, `PDMSUP0CSTSUPPCSMSUPPLIERTYPE`, `PDMSUP0CSTSUPPCSMSUPPLIERCODE` | [`PDMSUP0`](../PDM/PDMSUP0.md) | `COMPANYCODE`, `AFRECTYCODE`, `AFTPREC`, `AFCITEM`, `AFVERNR`, `AFVERST`, `CSTSUPPCUSTOMERSUPPLIERTYPE`, `CSTSUPPCUSTOMERSUPPLIERCODE` | RESTRICT | `PDMSUP2.PDMSUP0COMPANYCODE = PDMSUP0.COMPANYCODE AND PDMSUP2.PDMSUP0AFRECTYCODE = PDMSUP0.AFRECTYCODE AND PDMSUP2.PDMSUP0AFTPREC = PDMSUP0.AFTPREC AND PDMSUP2.PDMSUP0AFCITEM = PDMSUP0.AFCITEM AND PDMSUP2.PDMSUP0AFVERNR = PDMSUP0.AFVERNR AND PDMSUP2.PDMSUP0AFVERST = PDMSUP0.AFVERST AND PDMSUP2.PDMSUP0CSTSUPPCSMSUPPLIERTYPE = PDMSUP0.CSTSUPPCUSTOMERSUPPLIERTYPE AND PDMSUP2.PDMSUP0CSTSUPPCSMSUPPLIERCODE = PDMSUP0.CSTSUPPCUSTOMERSUPPLIERCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PDMSUP2UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PDMSUP0COMPANYCODE,
       t.PDMSUP0AFRECTYCODE,
       t.PDMSUP0AFTPREC,
       t.PDMSUP0AFCITEM,
       t.PDMSUP0AFVERNR,
       t.PDMSUP0AFVERST,
       t.PDMSUP0CSTSUPPCSMSUPPLIERTYPE,
       t.PDMSUP0CSTSUPPCSMSUPPLIERCODE,
       t.AF_SIZESIZESTYPECODE,
       t.AF_SIZECODE,
       t.AF_SIZCD,
       t.AF_SIZDS
FROM   DB2ADMIN.PDMSUP2 t
FETCH FIRST 100 ROWS ONLY;
```
