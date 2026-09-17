# DB2ADMIN.INTERNALPICKING

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 26230

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `PICKINGDATE` | DATE |  |  |  |  |
| 7 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  | FK | foreign_key |  |
| 8 | `STATUS` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 15 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INTERNALPICKING.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALPICKING.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND INTERNALPICKING.COUNTERCODE = COUNTER.CODE` |
| `PHYSICALWAREHOUSE_PHYSICALWAREHOUSE` | `PHYSICALWAREHOUSECOMPANYCODE`, `PHYSICALWAREHOUSECODE` | [`PHYSICALWAREHOUSE`](../CORE_MASTER/PHYSICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALPICKING.PHYSICALWAREHOUSECOMPANYCODE = PHYSICALWAREHOUSE.COMPANYCODE AND INTERNALPICKING.PHYSICALWAREHOUSECODE = PHYSICALWAREHOUSE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `INTERNALPICKING_PICKING` | [`INTERNALDOCUMENTLINE`](../INTERNAL_ORDERS/INTERNALDOCUMENTLINE.md) | `INTERNALDOCUMENTCOMPANYCODE`, `PICKINGCOUNTERCODE`, `PICKINGCODE` | `INTERNALDOCUMENTLINE.INTERNALDOCUMENTCOMPANYCODE = INTERNALPICKING.COMPANYCODE AND INTERNALDOCUMENTLINE.PICKINGCOUNTERCODE = INTERNALPICKING.COUNTERCODE AND INTERNALDOCUMENTLINE.PICKINGCODE = INTERNALPICKING.CODE` |

## Indexes

- `INTERNALPICKINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.PICKINGDATE,
       t.PHYSICALWAREHOUSECODE,
       t.STATUS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.INTERNALPICKING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
