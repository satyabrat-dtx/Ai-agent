# DB2ADMIN.PDMCO1

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `CORECTYCODE`, `COTPREC`, `COCITEM`, `COVERNR`, `COVERST`, `COGRPCO`, `COCDCOL`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 80215

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CORECTYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `COTPREC` | DECIMAL(1,0) | NOT NULL | PK | primary_key |  |
| 3 | `COCITEM` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `COVERNR` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `COVERST` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `COGRPCO` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `COCDCOL` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `COANNUL` | CHAR(1) |  |  |  |  |
| 9 | `COTKGRP` | CHAR(1) |  |  |  |  |
| 10 | `COCMGRP` | CHAR(1) |  |  |  |  |
| 11 | `COERPGR` | CHAR(2) |  |  |  |  |
| 12 | `CORECTYCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PDMCO1.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_CORECTY` | `CORECTYCOMPANYCODE`, `CORECTYCODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PDMCO1.CORECTYCOMPANYCODE = ITEMTYPE.COMPANYCODE AND PDMCO1.CORECTYCODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PDMCO1_CMP` | [`PDMCO2`](../PDM/PDMCO2.md) | `PDMCO1COMPANYCODE`, `PDMCO1CORECTYCODE`, `PDMCO1COTPREC`, `PDMCO1COCITEM`, `PDMCO1COVERNR`, `PDMCO1COVERST`, `PDMCO1COGRPCO`, `PDMCO1COCDCOL` | `PDMCO2.PDMCO1COMPANYCODE = PDMCO1.COMPANYCODE AND PDMCO2.PDMCO1CORECTYCODE = PDMCO1.CORECTYCODE AND PDMCO2.PDMCO1COTPREC = PDMCO1.COTPREC AND PDMCO2.PDMCO1COCITEM = PDMCO1.COCITEM AND PDMCO2.PDMCO1COVERNR = PDMCO1.COVERNR AND PDMCO2.PDMCO1COVERST = PDMCO1.COVERST AND PDMCO2.PDMCO1COGRPCO = PDMCO1.COGRPCO AND PDMCO2.PDMCO1COCDCOL = PDMCO1.COCDCOL` |

## Indexes

- `PDMCO1UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CORECTYCODE,
       t.COTPREC,
       t.COCITEM,
       t.COVERNR,
       t.COVERST,
       t.COGRPCO,
       t.COCDCOL,
       t.COANNUL,
       t.COTKGRP,
       t.COCMGRP,
       t.COERPGR
FROM   DB2ADMIN.PDMCO1 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
