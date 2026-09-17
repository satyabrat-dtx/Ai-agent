# DB2ADMIN.PDMSUP1

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `PDMSUP0COMPANYCODE`, `PDMSUP0AFRECTYCODE`, `PDMSUP0AFTPREC`, `PDMSUP0AFCITEM`, `PDMSUP0AFVERNR`, `PDMSUP0AFVERST`, `PDMSUP0CSTSUPPCSMSUPPLIERTYPE`, `PDMSUP0CSTSUPPCSMSUPPLIERCODE`, `AF_COLORUSERGENGROUPTYPECODE`, `AF_COLORCODE`, `AF_ATCDKE1`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 48111

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
| 8 | `AF_COLORUSERGENGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 9 | `AF_COLORCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `AF_ATCDKE1` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `AF_COLCD` | CHAR(50) |  |  |  |  |
| 12 | `AF_COLDS` | VARCHAR(255) |  |  |  |  |
| 13 | `AF_COLORUSERGENGRPTYPECMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PDMSUP0_COLSEC` | `PDMSUP0COMPANYCODE`, `PDMSUP0AFRECTYCODE`, `PDMSUP0AFTPREC`, `PDMSUP0AFCITEM`, `PDMSUP0AFVERNR`, `PDMSUP0AFVERST`, `PDMSUP0CSTSUPPCSMSUPPLIERTYPE`, `PDMSUP0CSTSUPPCSMSUPPLIERCODE` | [`PDMSUP0`](../PDM/PDMSUP0.md) | `COMPANYCODE`, `AFRECTYCODE`, `AFTPREC`, `AFCITEM`, `AFVERNR`, `AFVERST`, `CSTSUPPCUSTOMERSUPPLIERTYPE`, `CSTSUPPCUSTOMERSUPPLIERCODE` | RESTRICT | `PDMSUP1.PDMSUP0COMPANYCODE = PDMSUP0.COMPANYCODE AND PDMSUP1.PDMSUP0AFRECTYCODE = PDMSUP0.AFRECTYCODE AND PDMSUP1.PDMSUP0AFTPREC = PDMSUP0.AFTPREC AND PDMSUP1.PDMSUP0AFCITEM = PDMSUP0.AFCITEM AND PDMSUP1.PDMSUP0AFVERNR = PDMSUP0.AFVERNR AND PDMSUP1.PDMSUP0AFVERST = PDMSUP0.AFVERST AND PDMSUP1.PDMSUP0CSTSUPPCSMSUPPLIERTYPE = PDMSUP0.CSTSUPPCUSTOMERSUPPLIERTYPE AND PDMSUP1.PDMSUP0CSTSUPPCSMSUPPLIERCODE = PDMSUP0.CSTSUPPCUSTOMERSUPPLIERCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PDMSUP1UID` (ABSUNIQUEID)

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
       t.AF_COLORUSERGENGROUPTYPECODE,
       t.AF_COLORCODE,
       t.AF_ATCDKE1,
       t.AF_COLCD
FROM   DB2ADMIN.PDMSUP1 t
FETCH FIRST 100 ROWS ONLY;
```
